import pyDes

# For Python3, you'll need to use bytes, i.e.:
s=input("digite um texto para criptografar\n")
data = str.encode(s)
k = pyDes.triple_des(b"CHAVE001CHAVE002CHAVE003", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

d = k.encrypt(data)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
assert k.decrypt(d) == data

