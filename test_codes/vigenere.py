s = "abcdef"
key = "HM"
newS = ""
count = 0

for char in s:
    b_char = char.encode("utf-8")[0]
    key_char = key[count % len(key)]
    b_key = key_char.encode("utf-8")[0]

    print(key_char, " KEY ", format(b_key, "08b"))
    print(char,     " CHR ", format(b_char, "08b"))

    b_xor = b_char ^ b_key
    print(chr(b_xor), " RLT ", format(b_xor, "08b"))
    print()

    newS += chr(b_xor)

    count += 1

print("\nFinal:", newS)