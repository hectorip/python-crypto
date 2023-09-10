# Shake es una función hash que puede generar hashes de cualquier longitud
# se puede pedir un hash de 128 bits, 256 bits, 512 bits, etc.
# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf

from hashlib import shake_128, shake_256

c = "hola, este es mi mensaje y esto es todo lo que quiero hashearñ".encode("utf-8")
h1 = shake_128(c)
h2 = shake_256(c)

print(f"c:  {c}")
print(f"Shake 128 hexadecimal:  {h1.hexdigest(128)}")
print(f"Longitud SHAKE 128 {len(h1.hexdigest(128))}")

print(f"Shake 256 hexadecimal:  {h1.hexdigest(32)}")
print(f"Longitud 256 {len(h2.hexdigest(32))}")
