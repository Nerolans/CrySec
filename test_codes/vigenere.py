s = "abcdef"
key = "bbcdef"
newS = ""
count = 0

for char in s:
    key_char = key[count % len(key)]
    char = char.lower()
    k = ord(key_char)-97
    c = ord(char)-97
    newC = ((k + c)%26)+65
    print(chr(newC), " RLT ")

    newS += chr(newC)
    count += 1

print("\nFinal:", newS)