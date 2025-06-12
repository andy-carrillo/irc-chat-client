import socket
import threading

# ==== CONFIGURACIÓN ====
SERVER = "irc.irc-hispano.org"
PORT = 6667
NICK = "Hipopotamo_c"       # Cámbialo por tu nick deseado
CHANNEL = "#prueba_c"       # Canal inicial (puedes cambiarlo con /j)

irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc_socket.connect((SERVER, PORT))

# === Enviar nick y user al conectar ===
irc_socket.send(f"NICK {NICK}\r\n".encode("utf-8"))
irc_socket.send(f"USER {NICK} 0 * :Python IRC Client\r\n".encode("utf-8"))

channel_actual = CHANNEL
privado_actual = None  # Si está activo, enviamos mensaje privado

# === Función para recibir mensajes ===
def receive_messages():
    global channel_actual
    while True:
        try:
            response = irc_socket.recv(2048).decode("utf-8", errors="ignore")
            for line in response.strip().split("\r\n"):
                print(line)

                # Responder al PING para evitar desconexión
                if line.startswith("PING"):
                    pong_response = line.replace("PING", "PONG")
                    irc_socket.send(f"{pong_response}\r\n".encode("utf-8"))

                # Hacer JOIN solo cuando se recibe el código de bienvenida (001)
                if " 001 " in line:
                    irc_socket.send(f"JOIN {channel_actual}\r\n".encode("utf-8"))

        except Exception as e:
            print(f"Error recibiendo mensajes: {e}")
            break

# === Lanzar hilo de recepción ===
threading.Thread(target=receive_messages, daemon=True).start()

# === Bucle principal para enviar comandos o mensajes ===
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
                print(f"(Abriendo conversación privada con {privado_actual}...)")

            elif cmd == "/back":
                privado_actual = None
                print(f"(Volviendo al canal {channel_actual}...)")

            elif cmd in ["/q", "/quit"]:
                irc_socket.send("QUIT :Adiós!\r\n".encode("utf-8"))
                break

            else:
                print("Comando no reconocido.")

        else:
            # Enviar mensaje al canal o al privado si está activo
            destino = privado_actual if privado_actual else channel_actual
            irc_socket.send(f"PRIVMSG {destino} :{msg}\r\n".encode("utf-8"))

except KeyboardInterrupt:
    print("\nDesconectando...")
    irc_socket.send("QUIT :Hasta la próxima!\r\n".encode("utf-8"))
    irc_socket.close()
