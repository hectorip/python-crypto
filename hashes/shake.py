# Shake es una función hash que puede generar hashes de cualquier longitud
# se puede pedir un hash de 128 bits, 256 bits, 512 bits, etc.
# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf

from hashlib import shake_128, shake_256
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

c = "hola, este es mi mensaje y esto es todo lo que quiero hashearñ".encode("utf-8")
h1 = shake_128(c)
h2 = shake_256(c)

logging.debug(f"c:  {c}")
logging.debug(f"Shake 128 hexadecimal:  {h1.hexdigest(128)}")
logging.debug(f"Longitud SHAKE 128 {len(h1.hexdigest(128))}")

logging.debug(f"Shake 256 hexadecimal:  {h1.hexdigest(32)}")
logging.debug(f"Longitud 256 {len(h2.hexdigest(32))}")
