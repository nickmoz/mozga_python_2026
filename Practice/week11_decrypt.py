from cryptography.fernet import Fernet

file = open('select.key', 'rb')
key = file.read()

enc = Fernet(key)

encrypted = 'gAAAAABq_r12KRLqTzxs0MvXY6s290sPM7xYZo6FhY_A_9sNXUVMscwly1fdpSjM3z9xIdY7cBf_YYUQL7Vl064-f4SVDAjSiQ=='

message = enc.decrypt(encrypted).decode()

print(message)
