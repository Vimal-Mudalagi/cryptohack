

# if p and q are prime their gcd is always one

Alright this is classic **Extended Euclid**—super important for crypto. Let’s go clean and fast.

---

## 🧠 First: what’s gcd(p, q)?

You’re given:

* p = 26513
* q = 32321
  Both are **prime**

👉 So:

```
gcd(p, q) = 1
```

No debate. Primes don’t share factors.

---

## 🎯 Goal

Find integers **u, v** such that:

```
p·u + q·v = 1
```

---

## 🚀 Final Answer (after Extended Euclid)

```
u = 10245
v = -8404
```

Check:

```
26513(10245) + 32321(-8404) = 1 ✔️
```

---

## 🏁 What to submit

They said:

> enter the LOWER number

👉 Between:

* 10245
* -8404

Answer:

```
-8404
```

---

## ⚡ Why this matters (don’t ignore this)

This `u` is basically:

```
u ≡ p⁻¹ mod q
```

👉 That’s **modular inverse**

Which is EXACTLY what you use in:

* RSA private key generation
* Decryption

---

## 🧠 Big picture

Extended GCD gives you:

* gcd (obvious)
* AND the coefficients (powerful)

Normal GCD → tells you “1”
Extended GCD → tells you **HOW to make 1**

That “how” = crypto magic.

---

