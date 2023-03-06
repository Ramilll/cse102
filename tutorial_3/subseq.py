def subseq(seq: list) -> list:
    """Generator that given a list seq yields all possible sublists of it"""
    n = len(seq)
    for i in range(2**n):
        yield [seq[j] for j in range(n) if (i >> j) & 1]
