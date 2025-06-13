import os
from datetime import datetime

BASE_DIR = "logs"

def guardar_mensaje_privado(usuario, mensaje):
    ruta = os.path.join(BASE_DIR, "privados")
    os.makedirs(ruta, exist_ok=True)
    archivo = os.path.join(ruta, f"{usuario}.txt")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {mensaje}\n")

def leer_historial(usuario, max_lineas=100):
    archivo = os.path.join(BASE_DIR, "privados", f"{usuario}.txt")
    if not os.path.isfile(archivo):
        return []
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return lineas[-max_lineas:]

def guardar_log_sistema(mensaje):
    ruta = os.path.join(BASE_DIR, "sistema")
    os.makedirs(ruta, exist_ok=True)
    archivo = os.path.join(ruta, "server_log.txt")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {mensaje}\n")
