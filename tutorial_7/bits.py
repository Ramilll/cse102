def uint16_to_bitstring(x: int):
    answer = [0] * 16
    counter = 0
    while x > 0:
        answer[counter] = x % 2
        counter += 1
        x = x // 2
    return answer[::-1]


def bitstring_to_uint16(bs):
    answer = 0
    for i in range(16):
        answer += bs[i] * (2 ** (15 - i))
    return answer


def mod_pow2(x, k):
    "Return x mod 2**k"
    return x & ((1 << k) - 1)


def is_pow2(x):
    "Return True if x is a power of 2"
    return x != 0 and (x & (x - 1)) == 0


def set_mask(w, m):
    """set every bit position which is 1 in m, to 1 in w"""
    return w | m


def toggle_mask(w, m):
    """toggle every bit position which is 1 in m, in w"""
    return w ^ m


def clear_mask(w, m):
    """set every bit position which is 1 in m, to 0 in w"""
    return w & ~m
