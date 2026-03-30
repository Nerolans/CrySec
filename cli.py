import argparse

#SHIFT / CAESAR CYPHER################################################
def shift():
    msg = input("Enter the text to Encode: ")
    key = int(input("key (Should be an Integer) : "))
    newMsg = ""

    for char in msg:
        if (ord(char) <= 90 and ord(char) >= 65):
            newMsg += chr(65 + ((ord(char) + key) - 65) % 26)
        elif (ord(char) <= 122 and ord(char) >= 97):
            newMsg += chr(97 + ((ord(char) + key) - 97) % 26)
        else:
            newMsg += char

    print("Your encoded message: " + newMsg)

#XOR############################################################################
def xor():
    msg = input("Enter the text to Encode: ")
    key = int(input("key (Should be a String) : "))
    count = 0
    newMsg = ""
    for char in msg:
        b_char = char.encode("utf-8")[0]
        key_char = key[count % len(key)]
        b_key = key_char.encode("utf-8")[0]

        print(key_char, " KEY ", format(b_key, "08b"))
        print(char, " CHR ", format(b_char, "08b"))

        b_xor = b_char ^ b_key
        print(chr(b_xor), " RLT ", format(b_xor, "08b"))
        print()

        newMsg += chr(b_xor)

        count += 1
    print("Your encoded message: " + newMsg)

#MENU#############################################################################
def menu(encodingOptions):
    print("\n--- CHOOSE THE ENCODING METHOD ---")
    for number, function in encodingOptions.items():
        # .__name__ récupère le nom de la fonction proprement
        print(f"{number}. Encode a message with: {function.__name__}")
    print("q. to quit the program")

#DEFAULT############################################################################
def main():
    # linking function to numbers in an array to limit the choice for the input and for chossing
    encodingOptions = {
        "1": shift,
        "2": xor
    }

    while True:
        #displaying the menu
        menu(encodingOptions)
        #storing the choice of the user
        defNumber = input("\nChoice > ").lower()

        #if user wants to quit
        if defNumber == 'q':
            break

        if defNumber in encodingOptions:
            #executing the correct function
            encodingOptions[defNumber]()
        else:
            print(f"'{defNumber}' is not a valid option")

if __name__ == "__main__":
    main()