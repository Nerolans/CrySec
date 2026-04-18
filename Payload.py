from enum import Enum

class PayloadType(Enum):
    SERVER = b's'
    TEXT = b't'
    RSA = b'r'
    DH = b'd'

class PayloadHandler:
    HEADER = b"ISC"


    def build_payload(msg_type: PayloadType, text: str) -> bytes:
        encoded_msg = text.encode('utf-32-be')
        length = (len(encoded_msg) // 4).to_bytes(2, byteorder='big')

        return PayloadHandler.HEADER + msg_type.value + length + encoded_msg

    def parse_payload(data: bytes):
        if len(data) < 6: return None, ""
        header = data[0:3]
        msg_type = data[3:4]
        payload_bytes = data[6:]
        text = payload_bytes.decode('utf-32-be', errors='replace')
        return msg_type, text