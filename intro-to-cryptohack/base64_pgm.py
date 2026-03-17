import base64

hex_data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: hex → bytes
raw_bytes = bytes.fromhex(hex_data)

# Step 2: bytes → Base64
b64 = base64.b64encode(raw_bytes)

print(b64.decode())