import socket
import threading
import sys
from Payload import PayloadHandler, PayloadType

class NetworkClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.is_connected = False
        self.callback = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.is_connected = True
        print("Connected")

    def disconnect(self):
        self.is_connected = False
        if self.socket:
            self.socket.close()
            print("Deconnected")

    def send(self, msg_type, text):
        message_binaire = PayloadHandler.build_payload(msg_type, text)
        self.socket.sendall(message_binaire)


    def set_callback(self, callback):
        self.callback = callback

    def start_listening(self):
        if not self.is_connected:
            print("Erreur: Non connecté au serveur.")
            return

        thread = threading.Thread(target=self._receive_loop, daemon=True)
        thread.start()

    def _receive_loop(self):

        while self.is_connected:
            try:
                reponse_brute = self.socket.recv(4096)
                if not reponse_brute:
                    break

                msg_type, text = PayloadHandler.parse_payload(reponse_brute)
                if self.callback:
                    self.callback(msg_type, text)
                else:
                    sys.stdout.write('\r\033[K')
                    print(f"[Reçu] : {text}")
                    sys.stdout.write('> ')
                    sys.stdout.flush()

            except Exception as e:
                if self.is_connected:
                    print(f"\n[Erreur de réception] {e}")
                break

        self.disconnect()