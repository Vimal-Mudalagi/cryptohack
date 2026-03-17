from binascii import unhexlify

# given hex values
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_xor_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_xor_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_xor_all = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# convert hex -> bytes
KEY1 = unhexlify(KEY1)
KEY2_xor_KEY1 = unhexlify(KEY2_xor_KEY1)
KEY2_xor_KEY3 = unhexlify(KEY2_xor_KEY3)
FLAG_xor_all = unhexlify(FLAG_xor_all)

# helper for XOR
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# recover keys
KEY2 = xor_bytes(KEY2_xor_KEY1, KEY1)
KEY3 = xor_bytes(KEY2_xor_KEY3, KEY2)

# recover flag
FLAG = xor_bytes(FLAG_xor_all, KEY1)
FLAG = xor_bytes(FLAG, KEY2)
FLAG = xor_bytes(FLAG, KEY3)

print(FLAG.decode())