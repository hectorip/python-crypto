# AES-GCM (Galois Counter Mode)

import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Instatiating a new AES-GCM cipher

c = Cipher(algorithms.AES(secrets.token_bytes(32)), modes.GCM(secrets.token_bytes(12)))
