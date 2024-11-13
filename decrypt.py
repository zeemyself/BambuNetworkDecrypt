from Crypto.Cipher import AES

key = b"i4crL3LESLnWapLS"

with open('BambuNetworkEngine.conf', 'rb') as f:
    cfg_data = f.read()

cipher = AES.new(key, AES.MODE_ECB)

de_data = b''
pos = 0
while pos < len(cfg_data):
    decrypted_block = cipher.decrypt(cfg_data[pos:pos+16])
    de_data += decrypted_block
    pos += 16

with open('decrypted.conf', 'wb') as f:
    f.write(de_data)