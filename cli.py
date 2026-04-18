from Servers_tests import *

from Servers_tests import run_server_task

def main():
    while True:
        print("\n--- SECURE CHAT ---")
        print("1. Test SHIFT")
        print("2. Test VIGENERE")
        print("3. Test XOR ")
        print("q. Quitter")

        choix = input("\n> ")

        if choix == "1":
            run_server_task("shift")
        elif choix == "2":
            run_server_task("vigenere")
        elif choix == "3":
            # On teste la variante sym-xor qui est souvent la bonne
            run_server_task("sym-xor")
        elif choix == "q":
            break

if __name__ == "__main__":
    main()