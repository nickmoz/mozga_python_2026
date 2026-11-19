from cryptography.fernet import Fernet

file = open('select.key', 'rb')
key = file.read()

enc = Fernet(key)

message = input("Type your message: ")
encrypted_message = enc.encrypt(message.encode())

print(encrypted_message)
