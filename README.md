# 💬 IRC Chat Client (WebSocket + HTML)

Un cliente IRC ligero escrito en Python y HTML, inspirado en XChat y diseñado para conectarse a servidores como `irc.irc-hispano.org`.

## 📁 Estructura del Proyecto

```
irc-chat-client/
├── backend/
│   ├── irc_bridge.py
│   ├── websocket_server.py
│   └── logs/
│       ├── sistema/
│       └── privados/
├── frontend/
│   └── ws-test.html
├── requirements.txt
└── .gitignore
```

## 🚀 Requisitos

- Python 3.10 o superior
- `websockets` (ya incluido en `requirements.txt`)

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/andy-carrillo/irc-chat-client.git
   cd irc-chat-client
   ```

2. Crea un entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # En Windows: .venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

1. Ejecuta el servidor WebSocket en `backend/`:
   ```bash
   python backend/websocket_server.py
   ```

2. Abre el cliente HTML en tu navegador:
   ```bash
   open frontend/ws-test.html   # En Mac
   start frontend/ws-test.html  # En Windows
   ```

## 💡 Características

- Conexión en tiempo real a canales IRC
- Soporte para comandos `/join`, `/nick`, `/query`, `/quit`
- Visualización de nicks conectados al canal
- Interfaz web con soporte para scroll, Enter, y auto-scroll

## 📦 Dependencias

- websockets

## 📁 Exclusiones (ver .gitignore)

- `.venv/`
- `__pycache__/`
- `logs/`
- `.DS_Store`

## 🧠 Inspirado en

XChat, HexChat y herramientas clásicas de IRC.