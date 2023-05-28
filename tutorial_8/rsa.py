import random


def is_prime(n, k=32):
    if n <= 3:
        return n in [2, 3]
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x in [1, n - 1]:
            continue
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


def genprime(l):
    """Generate a prime number of roughly l bits."""

    n = random.getrandbits(l)
    n |= (1 << l - 1) | 1  # Set the MSB and LSB bits to 1

    # Try successive odd numbers until a prime is found
    i = 0
    while True:
        p = n + 2 * i
        if is_prime(p):
            return p
        i += 1


def genmod(p, q):
    """Generate an RSA public/secret key pair."""

    M = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2, phi)
        gcd, u, _ = egcd(e, phi)
        if gcd != 1:
            continue
        if u < 0:
            k = (-u // phi) + 1
            u += k * phi
        d = u

        return (M, e), d


def egcd(b, a):
    """Return a triple (gcd(b,a), u, v) such that u*b+v*a=gcd(b,a)."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def keygen(l):
    "Generates an RSA public/secret key pair of size l (in bits)."

    p = genprime(l // 2)
    q = genprime(l // 2)

    public_key, secret_key = genmod(p, q)

    return public_key, secret_key


def enc(message, public_key):
    M, e = public_key
    return pow(message, e, M)


def dec(cipher, public_key, secret_key):
    M, e = public_key
    return pow(cipher, secret_key, M)


def encmsg(s, public_key):
    return [enc(byte, public_key=public_key) for byte in s]


def decmsg(a, public_key, secret_key):
    decoded_bytes = [dec(byte, public_key=public_key, secret_key=secret_key) for byte in a]
    byte_str = bytes(decoded_bytes)
    return byte_str
