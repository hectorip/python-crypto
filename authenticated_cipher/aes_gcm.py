# AES-GCM (Galois Counter Mode)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import secrets

data = b"este es el mensaje que quiero cifrar y autenticar"
datos_no_autenticados = b"este es el mensaje que quiero cifrar pero no autenticar"
key = AESGCM.generate_key(bit_length=128)

# Instanciando el cifrador AESGCM
aes = AESGCM(key)


# El nonce es un valor que sólo se usa una vez,
# no tiene que ser aleatorio pero sí único
nonce = secrets.token_bytes(12)

ct = aes.encrypt(nonce, data, datos_no_autenticados)

print(f"Datos cifrados con tag de autenticación y datos asociados: {ct}")
