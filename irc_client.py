import socket
import threading
from colorama import Fore, init
from config import SERVER, PORT, NICK, CHANNEL
from message_handler import manejar_ping, manejar_privmsg, manejar_servidor, mostrar_historial
from utils.logger import guardar_mensaje_privado

init(autoreset=True)

irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc_socket.connect((SERVER, PORT))

irc_socket.send(f"NICK {NICK}\r\n".encode("utf-8"))
irc_socket.send(f"USER {NICK} 0 * :Python IRC Client\r\n".encode("utf-8"))

channel_actual = CHANNEL
privado_actual = None

def receive_messages():
    global channel_actual
    while True:
        try:
            response = irc_socket.recv(2048).decode("utf-8", errors="replace")
            for line in response.strip().split("\r\n"):
                if line.startswith("PING"):
                    manejar_ping(line, irc_socket)
                elif "PRIVMSG" in line:
                    manejar_privmsg(line, privado_actual)
                elif " 001 " in line:
                    irc_socket.send(f"JOIN {channel_actual}\r\n".encode("utf-8"))
                else:
                    manejar_servidor(line)
        except Exception as e:
            print(Fore.RED + f"Error recibiendo mensajes: {e}")
            break

threading.Thread(target=receive_messages, daemon=True).start()

try:
    while True:
        msg = input()
        if not msg:
            continue

        if msg.startswith("/"):
            parts = msg.split(" ", 1)
            cmd = parts[0].lower()

            if cmd == "/j" and len(parts) > 1:
                new_channel = parts[1].strip()
                irc_socket.send(f"JOIN {new_channel}\r\n".encode("utf-8"))
                channel_actual = new_channel
                privado_actual = None

            elif cmd == "/n":
                irc_socket.send(f"NAMES {channel_actual}\r\n".encode("utf-8"))

            elif cmd == "/nick" and len(parts) > 1:
                new_nick = parts[1].strip()
                irc_socket.send(f"NICK {new_nick}\r\n".encode("utf-8"))

            elif cmd == "/query" and len(parts) > 1:
                privado_actual = parts[1].strip()
                print(Fore.MAGENTA + f"(Abriendo conversación privada con {privado_actual}...)")
                mostrar_historial(privado_actual)

            elif cmd == "/back":
                privado_actual = None
                print(Fore.CYAN + f"(Volviendo al canal {channel_actual}...)")

            elif cmd in ["/q", "/quit"]:
                irc_socket.send("QUIT :Adiós!\r\n".encode("utf-8"))
                break

            else:
                print(Fore.RED + "Comando no reconocido.")

        else:
            destino = privado_actual if privado_actual else channel_actual
            irc_socket.send(f"PRIVMSG {destino} :{msg}\r\n".encode("utf-8"))
            if privado_actual:
                guardar_mensaje_privado(privado_actual, f"tú → {privado_actual}: {msg}")

except KeyboardInterrupt:
    print("\nDesconectando...")
    irc_socket.send("QUIT :Hasta la próxima!\r\n".encode("utf-8"))
    irc_socket.close()
