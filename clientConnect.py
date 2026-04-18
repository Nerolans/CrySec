import socket
from Payload import PayloadHandler, PayloadType


class NetworkClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print("Connected")

    def disconnect(self):
        if self.socket:
            self.socket.close()
            print("Disconnect")

    def send(self, msg_type, text):
        message_binaire = PayloadHandler.build_payload(msg_type, text)
        self.socket.sendall(message_binaire)
        print(f"⬆Message envoyé : '{text}'")

    def receive(self):
        print("En attente")
        reponse_brute = self.socket.recv(4096)
        return PayloadHandler.parse_payload(reponse_brute)