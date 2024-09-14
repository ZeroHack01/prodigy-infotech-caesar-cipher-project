#!/bin/python3/prodigy infortech
# Prodigy Infotech Internship Project
# ------------------------------------
# PRODIGY INFOTECH INTERNSHIP PROJECT
# ------------------------------------

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Loop through each character in the text
    for char in text:
        # Check if it's an uppercase letter
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if it's a lowercase letter
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result


# Main function to get user input and perform encryption/decryption
def main():
    print("Welcome to the Prodigy Infotech Internship Project!")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if operation == 'encrypt':
        print("Encrypted message:", caesar_cipher(message, shift, mode='encrypt'))
    elif operation == 'decrypt':
        print("Decrypted message:", caesar_cipher(message, shift, mode='decrypt'))
    else:
        print("Invalid operation selected.")


if __name__ == "__main__":
    main()
