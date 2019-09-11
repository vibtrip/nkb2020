def count_bits(x):
    num_bits = 0
    while x != 0:
        num_bits += (x & 1)
        x >>= 1

    return num_bits


print ( count_bits(10))

def parity(x):
    result = 0
    while x != 0:
        result ^= x & 1
        x >>= 1

    return result