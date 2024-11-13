
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"i4crL3LESLnWapLS"

with open('decrypted.conf', 'rb') as f:
    raw_data = f.read()

# Pad the data to be a multiple of 16 bytes
padded_data = pad(raw_data, AES.block_size)

cipher = AES.new(key, AES.MODE_ECB)
encrypted_data = cipher.encrypt(padded_data)

with open('BambuNetworkEngine.conf', 'wb') as f:
    f.write(encrypted_data)