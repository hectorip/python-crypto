import secrets

# Genera un número aleatorio de 32 bytes
print(secrets.token_bytes(32))

# Generando un pin de 4 dígitos
print(secrets.randbelow(10000))
