import asyncio
import websockets
from irc_bridge import IRCBridge

connected_clients = set()

SERVER = "irc.irc-hispano.org"
PORT = 6667
NICK = "Hipopotamo_c"
CHANNEL = "#prueba_c"

irc = IRCBridge(SERVER, PORT, NICK, CHANNEL)

async def broadcast(msg):
    print(f"[🔁 IRC → WS] {msg}")
    for client in connected_clients:
        try:
            await client.send(msg)
        except Exception as e:
            print(f"❌ Error al enviar a cliente WebSocket: {e}")

async def handler(websocket, path):
    print("🌐 Cliente WebSocket conectado")
    connected_clients.add(websocket)

    # ✅ Enviar los nicks si ya fueron recibidos
    nicks = irc.get_nicks()
    if nicks:
        await websocket.send(f"[NICKS] {'|'.join(nicks)}")

    try:
        async for message in websocket:
            print(f"[🟡 WS → IRC] {message}")
            if message.startswith("/join "):
                canal = message.split("/join", 1)[1].strip()
                irc.channel = canal
                irc.sock.send(f"JOIN {canal}\r\n".encode())
                await websocket.send(f"📡 Cambiado a canal {canal}")
            elif message.startswith("/nick "):
                nuevo = message.split("/nick", 1)[1].strip()
                irc.sock.send(f"NICK {nuevo}\r\n".encode())
                await websocket.send(f"👤 Nick cambiado a {nuevo}")
            elif message.startswith("/query "):
                nick = message.split("/query", 1)[1].strip()
                await websocket.send(f"💬 Iniciado privado con {nick}")
            elif message in ("/q", "/quit"):
                irc.sock.send("QUIT :Adiós!\r\n".encode())
                await websocket.send("👋 Desconectado del IRC")
                await websocket.close()
            else:
                irc.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("❌ Cliente WebSocket desconectado")
    finally:
        connected_clients.remove(websocket)

async def irc_listener():
    loop = asyncio.get_event_loop()
    irc.listen(callback=broadcast, loop=loop)

async def main():
    irc.connect()
    print(f"🟢 Conectado a {irc.server} en {irc.channel} como {irc.nick}")

    server = await websockets.serve(handler, "localhost", 8765)
    print("🟢 WebSocket activo en ws://localhost:8765")

    try:
        await asyncio.gather(
            irc_listener(),
            asyncio.Future()
        )
    finally:
        server.close()
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
