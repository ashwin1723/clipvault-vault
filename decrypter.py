from cryptography.fernet import Fernet

# Replace with your key from key.txt
key = b'R0DOPyrWlzJwZbdHPT-8i7ONC1opD6EdP4iQgLKdz6I=%'

# Initialize the cipher
cipher = Fernet(key)

# Read and decrypt the vault/secret.txt file
with open("vault/secret.txt", "rb") as f:
    for line in f:
        try:
            decrypted = cipher.decrypt(line.strip()).decode()
            print(decrypted)
        except Exception as e:
            print(f"Failed to decrypt: {e}")