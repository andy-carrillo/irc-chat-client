import socket
import threading
import asyncio

class IRCBridge:
    def __init__(self, server, port, nick, channel):
        self.server = server
        self.port = port
        self.nick = nick
        self.channel = channel
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.latest_nicks = []

    def connect(self):
        self.sock.connect((self.server, self.port))
        self.sock.send(f"NICK {self.nick}\r\n".encode())
        self.sock.send(f"USER {self.nick} 0 * :web client\r\n".encode())
        print(f"🟢 Conectando a {self.server} como {self.nick}...")

    def get_nicks(self):
        return self.latest_nicks

    def listen(self, callback=None, loop=None):
        def receive():
            joined = False
            while True:
                try:
                    response = self.sock.recv(2048).decode("utf-8", errors="ignore")
                    for line in response.strip().split("\r\n"):
                        print(f"[IRC] {line}")
                        if line.startswith("PING"):
                            self.sock.send(f"PONG {line.split()[1]}\r\n".encode())
                        elif "001" in line and not joined:
                            self.sock.send(f"JOIN {self.channel}\r\n".encode())
                            joined = True
                            print(f"🟢 JOIN enviado a {self.channel}")
                        elif "353" in line and callback and loop:
                            parts = line.split(":", 2)
                            if len(parts) >= 3:
                                nicks_raw = parts[2].strip()
                                nicks = nicks_raw.split()
                                self.latest_nicks = nicks
                                asyncio.run_coroutine_threadsafe(
                                    callback(f"[NICKS] {'|'.join(nicks)}"), loop
                                )
                        elif "PRIVMSG" in line and callback and loop:
                            asyncio.run_coroutine_threadsafe(
                                callback(line.strip()), loop
                            )
                except Exception as e:
                    print(f"❌ Error IRC: {e}")
                    break

        threading.Thread(target=receive, daemon=True).start()

    def send(self, msg):
        self.sock.send(f"PRIVMSG {self.channel} :{msg}\r\n".encode())
