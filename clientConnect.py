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

    def receive(self):
        print("En attente")
        reponse_brut = self.socket.recv(4096)
        return PayloadHandler.parse_payload(reponse_brut)


    def set_callback(self, callback):
        self.callback = callback
        print(callback)

    def start_listening(self,gui = None):
        if not self.is_connected:
            print("Erreur: Non connecté au serveur.")
            gui.append("Erreur: Non connecté au serveur.")
            return

        thread = threading.Thread(target=self._receive_loop,args=(gui,), daemon=True)
        thread.start()
        gui.append("lancement du thread")

    def _receive_loop(self,gui = None):
        while self.is_connected:

            try:
                reponse_brute = self.socket.recv(4096)
                if not reponse_brute:
                    gui.append(f"break")
                    break

                msg_type, text = PayloadHandler.parse_payload(reponse_brute)
                if self.callback:
                    gui.append(f"callback")
                    self.callback(msg_type, text)
                else:

                    print(f"[Reçu] : {text}")
                    gui.append(f"[Reçu] : {text}")



            except Exception as e:
                if self.is_connected:
                    print(f"\n[Erreur de réception] {e}")
                    gui.append(f"fin de la boucle while")
                break

        self.disconnect()