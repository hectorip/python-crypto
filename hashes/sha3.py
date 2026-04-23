from hashlib import sha3_256, sha1, md5

c = "hola, este es mi mensaje y esto es todo lo que quiero hashear".encode("utf-8")
c = b"hola esto es cadena de bytes"
# Explicar que hace encode
# la función encode() devuelve una cadena codificada en bytes
# Es equivalente a bytes(s, 'utf-8')
# o a usar b'cadena' directamente
h = sha3_256(c)
h_sha1 = sha1(c)

# '0000 0001' -> '01'
# '1010 1010' -> 'AA'
#
print(f"c:  {c}")
print(f"Resultado hexadecimal:  {h.hexdigest()}")
# logging.debug(f"Resultado raw:  {sha3_256(c).digest()}%b")
print(f"Longitud {len(h.hexdigest())}")
