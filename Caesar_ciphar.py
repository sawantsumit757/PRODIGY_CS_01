def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result


message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'E' for Encrypt or 'D' for Decrypt: ").upper()

if choice == 'E':
    print("Encrypted Message:", encrypt(message, shift))
elif choice == 'D':
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid choice")
