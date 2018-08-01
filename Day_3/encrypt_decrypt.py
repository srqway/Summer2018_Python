def main():
    selection = int(input("Press 1 for encrypt, 2 for decrypt: "))
    if selection == 1:
        encrypt()
    else:
        decrypt()

def encrypt():
    cipher= input("Enter plaintext: ")
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    print(text)

def decrypt(): #got to check the capital A
    cipher= input("Enter ciphertext: ")
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    print(text)

if __name__ == "__main__":
    main()
