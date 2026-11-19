
from cryptography.fernet import Fernet

key = Fernet.generate_key()

file = open('select.key', 'wb')
file.write(key)

print("Key generated")
