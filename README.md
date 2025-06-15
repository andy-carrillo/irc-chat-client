# 🌐 IRC Chat Web Client (WebSocket Edition)

Este proyecto es un cliente IRC moderno basado en WebSockets y HTML, inspirado en el estilo clásico de XChat. Permite conectarse a canales IRC, enviar mensajes, cambiar de canal, actualizar el nick y ver los usuarios conectados, todo desde el navegador.

---

## 🚀 Tecnologías usadas

- **Python 3.12+**
- **WebSockets (servidor backend con `websockets`)**
- **HTML + JS (cliente frontend)**
- **IRC Raw Protocol**
- Sin frameworks pesados — solo tecnologías básicas y eficientes.

---

## 📁 Estructura del proyecto

```
irc-chat-client/
├── backend/
│   ├── irc_bridge.py           # Lógica de conexión IRC
│   ├── websocket_server.py     # Servidor WebSocket que enlaza navegador y IRC
│   └── logs/                   # Logs separados: privados y sistema
├── frontend/
│   └── ws-test.html            # Interfaz web moderna
├── .gitignore
└── README.md
```

---

## ✅ Funcionalidades

- ✅ Conexión automática a `irc.irc-hispano.org`
- ✅ Cambio de canal con `/join #canal`
- ✅ Cambio de nick con `/nick NuevoNick`
- ✅ Mensajes privados con `/query nick`
- ✅ Salida con `/quit` o `/q`
- ✅ Visualización en tiempo real de:
  - Mensajes
  - Usuarios conectados (nicks)
  - Canales
- ✅ Soporte para logs locales

---

## 📦 Instalación

```bash
git clone https://github.com/andy-carrillo/irc-chat-client.git
cd irc-chat-client/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python websocket_server.py
```

Luego, abre `frontend/ws-test.html` en tu navegador.

---

## 📝 Notas

- Se conecta por defecto a `irc.irc-hispano.org` en el canal `#prueba_c` con el nick `Hipopotamo_c`.
- El código está optimizado para **uso educativo** y personal.
- Puedes modificar los valores por defecto desde `websocket_server.py`.

---

## 📂 .gitignore sugerido

```
.venv/
__pycache__/
logs/
```

---

## ✨ Captura

![Vista del cliente en navegador](docs/screenshot.png)

---

## 👨‍💻 Autor

Desarrollado por **Andres Carrillo** ([@andy-carrillo](https://github.com/andy-carrillo)) — Junio 2025.

---
