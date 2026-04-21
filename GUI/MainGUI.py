
import sys

from PyQt6 import uic, QtWidgets
from Gui import Ui_MainWindow


from Servers_tests import run_server_task
from test_codes.cypher import shift_encode, shift_findKey
from test_codes.vigenere import vigenere_encode


class ProjetCrypto(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProjetCrypto, self).__init__()
        uic.loadUi('Gui.ui', self)

        self.frame_Shift.hide()
        self.frame_Vigenere.hide()

        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame shift
        self.btn_mode_shift.clicked.connect(self.activer_shift)
        self.btn_shift_serverTest.clicked.connect(self.btn_test_shift)
        self.btn_shift_encode.clicked.connect(self.btn_encode_shift)
        self.btn_shift_decode.clicked.connect(self.btn_decode_shift)
        #-------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------
        # Bouton dans la frame vigenere
        self.btn_mode_vigenere.clicked.connect(self.activer_vigenere)
        self.btn_vigenere_serverTest.clicked.connect(self.btn_test_vigenere)
        self.btn_vigenere_encode.clicked.connect(self.btn_encode_vigenere)
        #-------------------------------------------------------------------------------------------------------------------

    # --- 3. LES FONCTIONS QUI FONT APPARAÎTRE/DISPARAÎTRE ---

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


#-------------------------------------------------------------------------------------------------------------------
# Fonction dans la frame shift
#-------------------------------------------------------------------------------------------------------------------
    def btn_encode_shift(self):
        msg = str(self.shift_text.toPlainText())
        key = str(self.shift_key.text())
        self.shift_result.append(shift_encode(msg, key))

    def btn_decode_shift(self):
        msg = str(self.shift_text.toPlainText())
        self.shift_result.append(f"the key is : {shift_findKey(msg)}")
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

# --- Lancement ---
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    fenetre = ProjetCrypto()
    fenetre.show()
    sys.exit(app.exec())