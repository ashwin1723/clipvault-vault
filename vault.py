from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

# Fixed salt for consistent key derivation
SALT = b'some_fixed_salt'

def derive_key(password: str) -> bytes:
    """Derive a key from the password using PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def lock_data(data: str, password: str) -> bytes:
    """Encrypt text using the password"""
    key = derive_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())

def unlock_data(encrypted: bytes, password: str) -> str:
    """Decrypt text using the password"""
    key = derive_key(password)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted).decode()