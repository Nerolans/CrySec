from Servers_tests import *

from Servers_tests import run_server_task, run_chat_mode

def main():
    while True:
        print("\n--- SECURE CHAT ---")
        print("1. SHIFT")
        print("2. VIGENERE")
        print("3. Test XOR ")
        print("4. HASH")
        print("5. RSA")
        print("6. Diffie-Hellman")
        print("7. Entrer dans le CHAT")
        print("q. Quitter")

        choix = input("\n> ")

        if choix == "1":
            run_server_task("shift")
        elif choix == "2":
            run_server_task("vigenere")
        elif choix == "3":
            run_server_task("sym-xor")
        elif choix == "4":
            run_server_hash()
        elif choix == "5":
            run_server_rsa()
        elif choix == "6":
            run_server_diffie()
        elif choix == "7":
            run_chat_mode()

        elif choix == "q":
            break

if __name__ == "__main__":
    main()