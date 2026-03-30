s = "abcdef"
key = "HM"
newS = ""
count = 0

for char in s:
    key_char = key[count % len(key)]

    b_xor = (ord(char) + ord(key_char)-65)%26
    b_xor += 65
    print(chr(b_xor), " RLT ", format(b_xor, "08b"))
    print()

    newS += chr(b_xor)

    count += 1

print("\nFinal:", newS)