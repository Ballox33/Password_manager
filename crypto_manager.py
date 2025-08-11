import base64
import os
import sqlite3
from utils import get_db_path
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# Salt fisso: puoi salvarlo in un file, ma NON cambiarlo dopo che hai salvato password
# il salt è una sequenza di byte usata per rendere le password più sicure
SALT = b'psw_salt'   #la b indica che è un byte string, utile per la crittografia

#funzione per generare una chiave di crittografia
def generate_key(master_password: str) -> bytes:
    """Genera una chiave Fernet partendo dalla master password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=390000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

def encrypt_password(master_password: str, plain_password: str) -> str:
    key = generate_key(master_password)
    f = Fernet(key)
    return f.encrypt(plain_password.encode()).decode()

def decrypt_password(master_password: str, encrypted_password: str) -> str:
    key = generate_key(master_password)
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

def check_master_password(master): 
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM passwords WHERE id_sito = "master" """)
    master_psw = cursor.fetchone()[1]
    conn.close()
    try:
        if decrypt_password(master, master_psw) == master:
            return True
    except InvalidToken:
        return False
    