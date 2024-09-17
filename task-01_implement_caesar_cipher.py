#task-01
#Implement Caesar Cipher
import string
alphabet=list(string.ascii_lowercase) 
#!functions
def encryption (message,shift):
    encrypted_message = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            encrypted_message += alphabet[new_position]
        else:
            encrypted_message += char
    return encrypted_message

def decryption(message,shift):
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift) % 26
            decrypted_message += alphabet[new_position]
        else :
            decrypted_message += char
    return decrypted_message
def output (encrypted_message):
    print("the encrypted message is << " + encrypted_message + " >>")

#?Main
message=input("Enter the message : ")
shift=int(input("Enter the shift value : "))
action=int(input("Enter 1 to encrypt or 2 to decrypt :"))
if action == 1:
    result = encryption(message, shift)
    print(f"Encrypted message: {result}")
elif action == 2:
    result = decryption(message, shift)
    print(f"Decrypted message: {result}")
else:
    print("Invalid action. Please try again.")