from colorama import Fore
from utils.logger import guardar_mensaje_privado, leer_historial, guardar_log_sistema

def manejar_ping(line, irc_socket):
    pong = line.replace("PING", "PONG")
    irc_socket.send(f"{pong}\r\n".encode("utf-8"))
    print(Fore.YELLOW + "[PING recibido → PONG enviado]")

def manejar_privmsg(line, privado_actual):
    prefix, command = line.split(" PRIVMSG ", 1)
    nick = prefix.split("!")[0][1:]
    destino, mensaje = command.split(" :", 1)

    if destino.startswith("#"):
        print(Fore.CYAN + f"[{nick} → {destino}] {mensaje}")
    else:
        print(Fore.MAGENTA + f"[PRIVADO de {nick}] {mensaje}")
        guardar_mensaje_privado(nick, f"{nick} → tú: {mensaje}")

def manejar_servidor(line):
    print(Fore.GREEN + f"[Servidor] {line}")
    if not line.startswith("PING"):
        guardar_log_sistema(line)

def mostrar_historial(usuario):
    historial = leer_historial(usuario)
    if historial:
        print(Fore.MAGENTA + f"(Últimos mensajes con {usuario}:)")
        for linea in historial:
            print(Fore.MAGENTA + linea.strip())
