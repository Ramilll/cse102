def tap_uint16(x, i):
    """Return 1 or 0 depending on whether the ith-least significant bit
    of x is 1 or 0.
    """
    return (x >> i) & 1


def polytap_uint16(x, I):
    """Tap x at all the positions in I (which is a list of tap
    positions) and return the xor of all of these tapped values.
    """
    answer = 0
    for i in I:
        answer ^= tap_uint16(x, i)
    return answer


def lfsr_uint16(x, I):
    """Return the successor of x in an LFSR based on tap positions I"""
    return (x >> 1) | (polytap_uint16(x, I) << 15)


def test_lfsr_uint16(seed):
    I = [0, 2, 3, 5, 15]
    xs = [seed]
    for _ in range(10):
        xs.append(lfsr_uint16(xs[-1], I))
    return xs
