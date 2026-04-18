from Servers_tests import *

from Servers_tests import run_server_task, run_chat_mode

def main():
    while True:
        print("\n--- SECURE CHAT ---")
        print("1. Test SHIFT")
        print("2. Test VIGENERE")
        print("3. Test XOR ")
        print("4. Entrer dans le CHAT")
        print("q. Quitter")

        choix = input("\n> ")

        if choix == "1":
            run_server_task("shift")
        elif choix == "2":
            run_server_task("vigenere")
        elif choix == "3":
            run_server_task("sym-xor")
        elif choix == "4":
            run_chat_mode()
        elif choix == "q":
            break

if __name__ == "__main__":
    main()