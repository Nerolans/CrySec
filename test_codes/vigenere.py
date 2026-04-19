def vigenere_encode(msg, key):
    result = ''
    for i in range(len(msg)):
        #each chr of the message
        char = msg[i]
        #extends the key if it's shorter than the message (repeats itself)
        key_char = key[i % len(key)]
        #get the character according to the vigenere table (basically adds both the key anf the chr number and laps around the alphabet if it's greater then 26)
        new_code = (ord(char) + ord(key_char)) % 256
        result += chr(new_code)

    return result

#WORK IN PROGRESS (seems like server want us to decode AND find the key from just the encoded message (pretty complicated)
def vigenere_decode(msg, key):
    result = ''
    for i in range(len(msg)):
        char = msg[i]
        key_char = key[i % len(key)]
        #same as encode but subtract the key value instead of adding it
        new_code = (ord(char) - ord(key_char)) % 256
        result += chr(new_code)
    return result