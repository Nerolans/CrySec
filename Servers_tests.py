import time

from clientConnect import NetworkClient
from Payload import PayloadHandler, PayloadType

from test_codes.cypher import shift_encode
from test_codes.cypher import shift_findKey

from test_codes.vigenere import vigenere_encode
from test_codes.XOR import XOR_encode

from test_codes.hash import *

from test_codes.Diffie import *

from test_codes.RSA import rsa_encode, rsa_decodeFirst, rsa_decodeSecond
import sys

ip_server = 'vlbelintrocrypto.hevs.ch'
port_server = 6000

def run_chat_mode():
    # 1. Configuration du client
    client = NetworkClient('vlbelintrocrypto.hevs.ch', 6000)

    # 2. On définit ce qu'on fait quand on reçoit un message
    def on_message(msg_type, text):
        # Efface la ligne actuelle (le "> "), affiche le message, et remet le "> "
        sys.stdout.write('\r\033[K')
        print(f"\r[Message Reçu] : {text}")
        sys.stdout.write('> ')
        sys.stdout.flush()

    client.set_callback(on_message)

    try:
        client.connect()
        client.start_listening() # LE THREAD SE LANCE ICI

        print("\n--- BIENVENUE DANS LE CHAT ---")
        print("(Tapez '/quit' pour revenir au menu principal)")

        # 3. Boucle d'envoi (le thread d'écoute tourne tout seul à côté)
        while True:
            msg = input("> ")

            if msg.lower() == '/quit':
                print("Retour au menu...")
                break

            if msg.strip():
                # On envoie le message au serveur
                client.send(PayloadType.TEXT, msg)

    except Exception as e:
        print(f"Erreur de connexion : {e}")
    finally:
        client.disconnect()

def run_server_task(algo_name: str,action,param = 6, gui=None):
    #action = input("Action (encode/decode) [default: encode]: ") or "encode"
    #param = input("Paramètre (ex: 6 ou 12) [default: 6]: ") or "6"

    full_command = f"task {algo_name} {action} {param}"
    client = NetworkClient(ip_server,port_server)
    try:
        client.connect()
        client.send(PayloadType.SERVER, full_command)

        msg_type, *_, instr = client.receive()
        print(f"Instruction: {instr}")
        gui.append(f"Instruction: {instr}")

        if "Unknown" in instr or "Wrong" in instr:
            return

        _, secret = client.receive()
        print(f"Secret: {secret}")
        gui.append(f"Secret: {secret}")

        words = instr.split()
        key = words[-1]

        if algo_name == "shift":
            if action == "encode":
                res = shift_encode(secret, int(key))
                gui.append(f"message encoder : {res}")
            elif action == "decode":
                res = str(shift_findKey(secret))
                gui.append(f"message encoder : {res}")

        elif algo_name == "vigenere":
            if action == "encode":
                res = vigenere_encode(secret, key)
                gui.append(f"message encoder : {res}")
            elif action == "decode":
                res = ""#vigenere_decode(secret, key)

        elif "xor" in algo_name:
            res = XOR_encode(secret, key)

        client.send(PayloadType.SERVER, res)
        _, verdict = client.receive()
        print(f"Verdict: {verdict}")
        gui.append(f"Verdict: {verdict}")

    finally:
        client.disconnect()

def run_server_hash():
    action = input("Action (hash/verify) [default: hash]: ") or "hash"
    full_command = f"task hash {action}"
    client = NetworkClient(ip_server, port_server)

    try:
        client.connect()
        client.send(PayloadType.SERVER, full_command)

        msg_type, *_, instr = client.receive()
        print(f"Instruction: {instr}")

        if "Unknown" in instr or "Wrong" in instr:
            return


        _, corrupted_secret = client.receive()
        secret = clean_secret(corrupted_secret)
        print(secret)
        print(f"Secret: {secret}")

        words = instr.split()
        key = words[-1]

        if action == "hash":
            res = hash_1(secret)
        elif action == "verify":
            res = ""
            #res = verify(secret,hash)

        client.send(PayloadType.SERVER, res)
        _, verdict = client.receive()
        print(f"Verdict: {verdict}")

    finally:
        client.disconnect()

def run_server_rsa():
    action = input("Action (encode/decode) [default: encode]: ") or "encode"
    param = input("Paramètre (ex: 6 ou 200) [default: 6]: ") or "6"
    full_command = f"task RSA {action} {param}"
    client = NetworkClient(ip_server, port_server)

    try:
        client.connect()
        client.send(PayloadType.SERVER, full_command)

        msg_type, *_, instr = client.receive()
        print(f"Instruction: {instr}")

        if "Unknown" in instr or "Wrong" in instr:
            return

        ##ici rien a recevoir si l'action est "decode"


        words = instr.split()
        key = words[-1]

        if action == "encode":
            _, secret = client.receive()
            print(f"Secret: {secret}")
            n = instr.split("n=")[1].split(", e")[0]
            e = instr.split("e=")[1]
            res = rsa_encode(secret, int(n), int(e))
        elif action == "decode":
            res = rsa_decodeFirst()
            n = res[0]
            e = res[1]
            d = res[2]
            client.send(PayloadType.SERVER, str(str(n)+","+str(e)))
            _, answer = client.receive()
            res = rsa_decodeSecond(answer,d,n)

        client.send(PayloadType.SERVER, res)
        _, verdict = client.receive()
        print(f"Verdict: {verdict}")

    finally:
        client.disconnect()

def run_server_diffie():
    full_command = f"task DifHel"
    client = NetworkClient(ip_server, port_server)

    try:
        client.connect()
        client.send(PayloadType.SERVER, full_command)

        msg_type, *_, instr = client.receive()
        print(f"Instruction: {instr}")

        if "Unknown" in instr or "Wrong" in instr:
            return

        words = instr.split()
        key = words[-1]

        #first part
        prime = generate_prime(1000,5000)
        generator = find_p_root(prime)
        res = str(prime)+","+str(generator)
        client.send(PayloadType.SERVER, res)
        _, answer = client.receive()
        print(answer)

        #second part (generate our own public key)
        _, b_public = client.receive()
        private = generate_private()
        a_public = generate_publicKey(prime,generator, private)
        client.send(PayloadType.SERVER, str(a_public))
        _, answer = client.receive()
        print(answer)

        #third part (generate secret)
        secret = calculate_secret(int(b_public), private, prime)
        client.send(PayloadType.SERVER, str(secret))
        _, answer = client.receive()
        print(answer)

    finally:
        client.disconnect()