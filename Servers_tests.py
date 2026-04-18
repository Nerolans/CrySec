from clientConnect import NetworkClient
from Payload import PayloadHandler, PayloadType
from test_codes.cypher import shift_encode
from test_codes.vigenere import vigenere_encode
from test_codes.XOR import XOR_encode


ip_server = 'vlbelintrocrypto.hevs.ch'
port_server = 6000

def run_server_task(algo_name: str):
    action = input("Action (encode/decode) [default: encode]: ") or "encode"
    param = input("Paramètre (ex: 6 ou 12) [default: 6]: ") or "6"

    full_command = f"task {algo_name} {action} {param}"
    client = NetworkClient(ip_server,port_server)
    try:
        client.connect()
        client.send(PayloadType.SERVER, full_command)

        msg_type, *_, instr = client.receive()
        print(f"Instruction: {instr}")

        if "Unknown" in instr or "Wrong" in instr:
            return

        _, secret = client.receive()
        print(f"Secret: {secret}")

        words = instr.split()
        key = words[-1]

        if algo_name == "shift":
            res = shift_encode(secret, int(key))
        elif algo_name == "vigenere":
            res = vigenere_encode(secret, key)
        elif "xor" in algo_name:
            res = XOR_encode(secret, key)

        client.send(PayloadType.SERVER, res)
        _, verdict = client.receive()
        print(f"Verdict: {verdict}")

    finally:
        client.disconnect()