# 💬 IRC Chat Client (Python)

Un cliente IRC ligero escrito en Python, inspirado en XChat y diseñado para conectarse a servidores como `irc.irc-hispano.org`.

---

## 🚀 Requisitos

- Python 3.6 o superior  
- Git y terminal (recomendado: Visual Studio Code)

---

## 📁 Estructura del proyecto

```
irc-chat-client/
├── irc_client.py          # Script principal
├── config.py              # Configuración general (host, puerto, nick)
├── commands.py            # Comandos personalizados (/j, /n, etc.)
├── message_handler.py     # Lógica de formato, colores y logs
├── utils/
│   └── logger.py          # Funciones para registrar logs
├── logs/
│   ├── privados/          # Mensajes privados por usuario
│   └── sistema/           # Mensajes del servidor (server_log.txt)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Uso

### 1. Clona el repositorio

```bash
git clone https://github.com/andy-carrillo/irc-chat-client.git
cd irc-chat-client
```

### 2. Crea y activa el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el cliente

```bash
python irc_client.py
```

---

## 🎮 Comandos disponibles

- `/j #canal` → Entrar al canal  
- `/n` → Ver usuarios del canal actual  
- `/nick NuevoNick` → Cambiar de nick  
- `/query usuario` → Abrir conversación privada  
- `/q` o `/quit` → Salir del servidor  

---

## 🧠 Funciones extra

- Colores para mensajes: servidor (verde), usuarios (cian), privados (magenta), PING/PONG (amarillo)  
- Guarda los últimos mensajes privados por usuario  
- Reabre histórico al volver a `/query usuario`  
- Guarda logs del servidor en `logs/sistema/server_log.txt`  
- Filtra mensajes PING/PONG de los logs  

---

## 🧪 Autenticación y reconexión (pendiente)

- Soporte para reconexión automática si el socket cae  
- Soporte futuro para autenticación con contraseña  

---

## 🤝 Autor

Desarrollado por [@andy-carrillo](https://github.com/andy-carrillo)  
Licencia MIT – 2025
