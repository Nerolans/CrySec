
import sys

from PyQt6 import uic, QtWidgets


from Servers_tests import run_server_task, run_server_hash, run_server_diffie, run_chat_mode
from test_codes.RSA import generate_keys, rsa_encode, transform_encoded_byte, rsa_decodeFirst, rsa_decodeSecond
from test_codes.cypher import shift_encode, shift_findKey, shift_decode
from test_codes.vigenere import vigenere_encode
from test_codes.hash import *
from test_codes.Diffie import *
from clientConnect import *
from Payload import PayloadHandler, PayloadType


class ProjetCrypto(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProjetCrypto, self).__init__()
        uic.loadUi('Gui.ui', self)
        self.chat_client = NetworkClient('vlbelintrocrypto.hevs.ch', 6000)

        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame shift
        self.btn_mode_shift.clicked.connect(self.activer_shift)
        self.btn_shift_serverTest.clicked.connect(self.btn_test_shift)
        self.btn_shift_encode.clicked.connect(self.btn_encode_shift)
        self.btn_shift_findKey.clicked.connect(self.btn_findKey_shift)
        self.btn_shift_decode.clicked.connect(self.btn_decode_shift)
        #-------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame vigenere
        self.btn_mode_vigenere.clicked.connect(self.activer_vigenere)
        self.btn_vigenere_serverTest.clicked.connect(self.btn_test_vigenere)
        self.btn_vigenere_encode.clicked.connect(self.btn_encode_vigenere)
        #-------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame Hash
        self.btn_mode_hash.clicked.connect(self.activer_hash)
        self.btn_hash_serverTest.clicked.connect(self.btn_test_hash)
        self.btn_hash_encode.clicked.connect(self.btn_encode_hash)
        self.btn_hash_verify.clicked.connect(self.btn_verify_hash)
        #-------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame chat mode
        self.btn_mode_chat.clicked.connect(self.activer_chat)
        self.btn_chat_send.clicked.connect(self.btn_send_chat)
        #-------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame RSA
        self.btn_mode_rsa.clicked.connect(self.activer_rsa)
        self.btn_rsa_serverTest.clicked.connect(self.btn_test_rsa)
        self.btn_rsa_encode.clicked.connect(self.btn_encode_rsa)
        self.btn_rsa_decode.clicked.connect(self.btn_decode_rsa)
        self.btn_rsa_generate.clicked.connect(self.btn_generate_rsa)
        #-------------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame Diffie
        self.btn_mode_diffie.clicked.connect(self.activer_diffHel)
        self.btn_DiffHel_connect.clicked.connect(self.btn_connect_diffHel)

        self.btn_DiffHel_direct.clecked.connect(self.btn_direct_diffHel)

        self.btn_DiffHel_part1_Send.clicked.connect(self.btn_part1_diffHel)
        self.btn_DiffHel_part2_Send.clicked.connect(self.btn_part2_diffHel)
        self.btn_DiffHel_part3_Send.clicked.connect(self.btn_part3_diffHel)

        self.btn_DiffHel_Generate1.clicked.connect(self.btn_first_diffHel)
        self.btn_DiffHel_Generate2.clicked.connect(self.btn_second_diffHel)
        self.btn_DiffHel_Generate3.clicked.connect(self.btn_final_diffHel)
        # -------------------------------------------------------------------------------------------------------------------
    def activer_shift(self):
        self.page_crypto.setCurrentIndex(0)
        self.print_server.clear()
        self.shift_result.clear()
        self.print_server.append("Mode SHIFT sélectionné")

    def activer_vigenere(self):
        self.page_crypto.setCurrentIndex(1)
        self.print_server.clear()
        self.vigenere_result.clear()
        self.print_server.append("Mode VIGENERE sélectionné")

    def activer_hash(self):
        self.page_crypto.setCurrentIndex(2)
        self.print_server.clear()
        self.hash_result.clear()
        self.print_server.append("Mode Hash sélectionné")

    def activer_rsa(self):
        self.page_crypto.setCurrentIndex(3)
        self.print_server.clear()
        self.rsa_text.clear()
        self.print_server.append("Mode RSA sélectionné")

    def activer_diffHel(self):
        self.page_crypto.setCurrentIndex(4)
        self.print_server.clear()
        self.print_server.append("Mode Diffie-hellman sélectionné")

    def activer_chat(self):
        self.page_crypto.setCurrentIndex(5)
        self.print_server.clear()
        self.chat_text.clear()
        self.print_server.append("Mode chat sélectionné")
        run_chat_mode(self.chat_client,self.print_server)




#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame shift
#-------------------------------------------------------------------------------------------------------------------
    def btn_encode_shift(self):
        msg = str(self.shift_text.toPlainText())
        key = int(self.shift_key.text())
        self.shift_result.append(shift_encode(msg, key))

    def btn_findKey_shift(self):
        msg = str(self.shift_text.toPlainText())
        self.shift_result.append(f"the key is : {shift_findKey(msg)}")

    def btn_decode_shift(self):
        msg = str(self.shift_text.toPlainText())
        key = int(self.shift_key.text())
        self.shift_result.append(shift_decode(msg, key))

    def btn_test_shift(self):
        msg_length = self.shift_length.value()
        if msg_length == 0:
            self.print_server.append("Choisir une taille !!!")

        if self.shift_encode.isChecked():
            action = "encode"
            run_server_task("shift",action,msg_length,self.print_server)

        elif self.shift_decode.isChecked():
            action = "decode"
            run_server_task("shift",action,msg_length,self.print_server)
        else:
            self.print_server.append("Choisir entre encode ou decode")
#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame vigenere
#-------------------------------------------------------------------------------------------------------------------
    def btn_encode_vigenere(self):
        msg = str(self.vigenere_text.toPlainText())
        key = str(self.vigenere_key.text())
        self.vigenere_result.append(vigenere_encode(msg, key))

    def btn_test_vigenere(self):
        msg_length = self.vigenere_length.value()
        if msg_length == 0:
            self.print_server.append("Choisir une taille !!!")

        if self.vigenere_encode.isChecked() == True:
            action = "encode"
            run_server_task("vigenere",action,msg_length,self.print_server)

        elif self.vigenere_decode.isChecked() == True :
            action = "decode"
            run_server_task("vigenere",action,msg_length,self.print_server)
        else:
            self.print_server.append("Choisir entre encode ou decode")
#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame Hash
#-------------------------------------------------------------------------------------------------------------------
    def btn_encode_hash(self):
        msg = str(self.hash_text.toPlainText())
        self.hash_result.append(hash_1(msg))
    def btn_verify_hash(self):
        msg = str(self.hash_text.toPlainText())
        hash = str(self.hash_result.toPlainText())
        if verify(msg, hash) == True :
            self.print_server.append("le hash est correct")
        else:
            self.print_server.append("le hash est incorrect")

    def btn_test_hash(self):
        if self.hash_encode.isChecked() == True:
            action = "hash"
            run_server_hash(action, self.print_server)
        if self.hash_verify.isChecked() == True:
            action = "verify"
            run_server_hash(action, self.print_server)
#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame chat
#-------------------------------------------------------------------------------------------------------------------
    def btn_send_chat(self):
        msg = str(self.chat_text.toPlainText())
        self.chat_client.send(PayloadType.TEXT, msg)
        self.chat_text.clear()
#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame RSA
#-------------------------------------------------------------------------------------------------------------------
    def btn_test_rsa(self):
        msg_length = self.rsa_length.value()
        if msg_length == 0:
            self.print_server.append("Choisir une taille !!!")

        if self.rsa_encode.isChecked() == True:
            action = "encode"
            run_server_task("RSA",action,msg_length,self.print_server)

        elif self.rsa_decode.isChecked() == True:
            action = "decode"
            run_server_task("RSA",action,msg_length,self.print_server)

        else:
            self.print_server.append("Choisir entre encode ou decode")

    def btn_encode_rsa(self):
        msg = str(self.rsa_text.toPlainText())
        publickey = int(self.rsa_publickey.text())
        modular = int(self.rsa_modular.text())
        msg_encoded_byte = rsa_encode(msg, modular, publickey)
        result = transform_encoded_byte(msg_encoded_byte)
        self.rsa_result.append(result)


    def btn_decode_rsa(self):
        msg_encoded = str(self.rsa_result.toPlainText())
        privatekey = int(self.rsa_privatekey.text())
        modular = int(self.rsa_modular.text())
        res = rsa_decodeSecond(msg_encoded,privatekey,modular)
        self.rsa_text.setText(str(res))

    def btn_generate_rsa(self):
        modular, publickey, privatekey = generate_keys()
        self.rsa_modular.setText(str(modular))
        self.rsa_publickey.setText(str(publickey))
        self.rsa_privatekey.setText(str(privatekey))


#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame Diffie-Hellman
#-------------------------------------------------------------------------------------------------------------------
    def btn_first_diffHel(self):
        prime = generate_prime(1000, int(self.DiffHel_max.text()))
        generator = find_p_root(prime)
        self.DiffHel_prime.setText(str(prime))
        self.DiffHel_generator.setText(str(generator))

    def btn_second_diffHel(self):
        private = generate_private()
        self.DiffHel_key_private.setText(str(private))
        a_public = generate_publicKey(self.DiffHel_prime.text(), self.DiffHel_generator.text(), private)
        self.DiffHel_key_public_a.setText(str(a_public))

    def btn_final_diffHel(self):
        secret = calculate_secret(int(self.DiffHel_key_public_b.text()), int(self.DiffHel_key_private.text()), int(self.DiffHel_prime.text()))
        self.DiffHel_secret.setText(str(secret))


    #Server
    def btn_direct_diffHel(self):
        run_server_task("init", self.print_server, self)

    def btn_connect_diffHel(self):
        run_server_diffie("init", self.print_server, self)

    def btn_part1_diffHel(self):
        run_server_diffie("first", self.print_server, self)

    def btn_part2_diffHel(self):
        run_server_diffie("second", self.print_server, self)

    def btn_part3_diffHel(self):
        run_server_diffie("third", self.print_server, self)

# --- Lancement ---
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    fenetre = ProjetCrypto()
    fenetre.show()
    sys.exit(app.exec())