from Cryptodome.Cipher import AES
from salted.settings import ENCRYPTION_KEY

def encrypt(s):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(str.encode(s))
    return cipher.nonce + tag + ciphertext

def decrypt(s):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_EAX, s[:16])
    return cipher.decrypt_and_verify(s[32:], s[16:32]).decode('UTF-8')
