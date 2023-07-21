# Ejemplo de uso de AES

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import secrets

key = b"Clave de 16 byte"
# una mejor clave sería:
key = secrets.token_bytes(16)
message = b"a" * 32

# Modos de trabajo de AES:
# ECB: Electronic Code Book
# CBC: Cipher Block Chaining

c = Cipher(algorithms.AES(key), modes.CBC(b"IV de 16 bytesss"))
ciphertext = c.encryptor().update(message)

print(ciphertext)
print(len(ciphertext))


# Using algorithms.AES with a 256-bit key:
key = secrets.token_bytes(256 // 8)
aes_256 = Cipher(
    algorithm=algorithms.AES256(key), mode=modes.CBC(secrets.token_bytes(128 // 8))
)
ciphertext = aes_256.encryptor().update(message)
print(ciphertext)
print(len(ciphertext))
