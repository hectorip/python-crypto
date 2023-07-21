from hashlib import sha3_256, sha1
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
c = "hola, este es mi mensaje y esto es todo lo que quiero hashearñ".encode("utf-8")
h = sha3_256(c)
h_sha1 = sha1(c)

logging.debug(f"c:  {c}")
logging.debug(f"Resultado hexadecimal:  {h}")
# logging.debug(f"Resultado raw:  {sha3_256(c).digest()}%b")
logging.debug(f"Longitud {len(h)}")
