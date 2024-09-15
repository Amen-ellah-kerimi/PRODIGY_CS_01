#task-01
#Implement Caesar Cipher

#!functions
def encryption (message,shift):
    import string
    alphabet=list(string.ascii_lowercase)
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
    import string
    alphabet=list(string.ascii_lowercase) 
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
message=input("input the message : ")
shift=int(input("input the shift value : "))
a=int(input("1 for encryption or 2 for decryption"))
if a==1:
    new_message=encryption(message,shift)
    print(new_message)
elif a==2:
    new_message=decryption(message,shift)
    print(new_message)