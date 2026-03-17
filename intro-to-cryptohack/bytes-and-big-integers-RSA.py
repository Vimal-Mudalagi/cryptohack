num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Step 1: convert to hex (remove '0x')
hex_str = hex(num)[2:]

# fix odd length (important edge case)
if len(hex_str) % 2:
    hex_str = '0' + hex_str

# Step 2: hex → bytes → string
message = bytes.fromhex(hex_str).decode()

print(message)


'''Mental model (lock this in)
Text = human view
Bytes = real data
Integer = math-friendly form


Because crypto (like RSA) does:

cipher = message^e mod n

👉 You can’t do math on strings
👉 You need a number'''