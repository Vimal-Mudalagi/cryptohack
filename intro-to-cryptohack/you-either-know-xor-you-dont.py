# Step 1: Convert hex → bytes (raw data)
data = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# Step 2: Known plaintext (CTF hint)
known = "crypto{"

# Step 3: Recover partial key using XOR
# key[i] = cipher[i] ^ plaintext[i]
key_bytes = [data[i] ^ ord(known[i]) for i in range(len(known))]

# Step 4: Convert key bytes → string
partial_key = ''.join(chr(b) for b in key_bytes)
print("Partial key:", partial_key)

# Step 5: Complete the key (based on pattern recognition)
# You noticed it's "myXORkey"
key = "myXORkey"

# Step 6: Decrypt full ciphertext using repeating key XOR
decoded = ''.join(
    chr(b ^ ord(key[i % len(key)]))  # repeat key using modulo
    for i, b in enumerate(data)
)

print("Decrypted message:", decoded)


'''
Your statement

You said:

cipher = key ^ plaintext

👉 That’s correct, but incomplete

Because:
👉 that only works if you're talking about one byte

🧠 2. Real situation: strings (multiple bytes)

A message isn’t one number, it’s:

plaintext = [p0, p1, p2, p3, ...]

A key (in this challenge) is:

key = [k0, k1, k2, ...]
⚡ 3. So encryption happens byte by byte
c0 = p0 ^ k0
c1 = p1 ^ k1
c2 = p2 ^ k2
...
🔥 4. Problem: key is shorter than message

Example:

plaintext:  p0 p1 p2 p3 p4 p5 p6 p7
key:        k0 k1 k2

👉 What happens after k2?

We repeat the key:

key:        k0 k1 k2 k0 k1 k2 k0 k1
🧠 5. That’s where this comes from:
cipher[i] = plaintext[i] ^ key[i % len(key)]
⚡ What does % do?
i % len(key)

👉 loops the index


So your formula becomes:

Instead of:

cipher = key ^ plaintext

👉 Real version:

cipher = byte-by-byte XOR with repeating key



Fix the key

Think:

myXORke → myXORkey

👉 That extra 'y' didn’t show because:

you only XORed "crypto{" (7 chars)

key length = 8



🧠 Insight (VERY IMPORTANT)
Known plaintext length < key length
→ you only recover partial key

So you must:
👉 guess the remaining part intelligently
'''        