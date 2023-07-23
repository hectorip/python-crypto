import secrets

# Genera un número aleatorio de 32 bytes
print(secrets.token_bytes(32))

# Generando un pin de 4 dígitos
print(secrets.randbelow(10000))

# Generación de números con la clase SystemRandom

system_random = secrets.SystemRandom()
print(system_random.randint(0, 10000))

# también sirve para elegir elementos aleatorios de una lista
print(system_random.choice(["a", "b", "c"]))
