# Una alternativa a SHA-256 es BLAKE2, más rápido
# pero menos estandarizado, por lo que no se puede aprovechar
# de la misma manera que SHA-256

# Sin embargo, es altamente paralelizable, por lo que es conveniente
# cuando hay que procesar muchos datos

from hashlib import blake2b

b = blake2b()
b.update(b"1234567890123456")

print("Blake 2b", b.hexdigest())
print("Longitud", len(b.digest()))
