# task-01
# Implement Caesar Cipher
# Author : Amen Ellah Kerimi
import string

alphabet = list(string.ascii_lowercase)

# functions
def encryption(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            alphabet = list(string.ascii_lowercase) if char.islower() else list(string.ascii_uppercase)
            position = alphabet.index(char.lower())
            new_position = (position + shift) % 26
            encrypted_message += alphabet[new_position] if char.islower() else alphabet[new_position].upper()
        else:
            encrypted_message += char  # Preserve non-alphabetic characters, including spaces
    return encrypted_message

def decryption(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            alphabet = list(string.ascii_lowercase) if char.islower() else list(string.ascii_uppercase)
            position = alphabet.index(char.lower())
            new_position = (position - shift) % 26
            decrypted_message += alphabet[new_position] if char.islower() else alphabet[new_position].upper()
        else:
            decrypted_message += char  # Preserve non-alphabetic characters, including spaces
    return decrypted_message

#* Main
message = input("Enter the message: ")
print("Note: Non-alphabetic characters have been removed from the input message, except for spaces.")

while True:
    try:
        shift = int(input("Enter the shift value: "))
        if shift <= 0:
            print("Shift value must be a positive integer. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

while True:
    try:
        action = int(input("Enter 1 to encrypt or 2 to decrypt: "))
        if action == 1 or action == 2:
            break
        else:
            print("Invalid action. Please enter 1 to encrypt or 2 to decrypt.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if action == 1:
    result = encryption(message, shift)
    print(f"Encrypted message: {result}")
elif action == 2:
    result = decryption(message, shift)
    print(f"Decrypted message: {result}")
