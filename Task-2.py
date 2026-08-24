from cryptography.fernet 
import Fernet

# Generate an encryption key
key = Fernet.generate_key()

print("Encryption Key:", key.decode())

cipher = Fernet(key)

# Get message
message = input("Enter message to encrypt: ")

# Convert text to bytes
message_bytes = message.encode()

# Display binary representation
binary = ' '.join(format(byte, '08b') for byte in message_bytes)

print("\nOriginal text:", message)
print("Binary:", binary)

# Encrypt
encrypted = cipher.encrypt(message_bytes)

print("\nEncrypted:", encrypted.decode())

# Decrypt
decrypted = cipher.decrypt(encrypted).decode()

print("\nDecrypted:", decrypted)