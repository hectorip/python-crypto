# ChaCha20 es una alternativa a AES, que es más rápido pero con menos
# garantías de seguridad úsalo si necesitas velocidad en un dispositivo
# con pocos recursos

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Se inicializa muy parecido a AES
c = Cipher(algorithms.ChaCha20(b"1234567890123456"), modes.CTR(b"123456789012"))
encryptor = c.encryptor()
print(encryptor.update(b"1234567890123456"))
