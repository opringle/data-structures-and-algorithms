
def get_bit(num: int, i: int) -> bool:
    """determine if bit at position i in binary representation
    of num is 1
    """
    return (num & (1 << i)) != 0

def set_bit(num: int, i: int) -> int:
    """
    Set the bit at position i in num to 1.
    """
    return num | (1 << i)

def clear_bit(num: int, i: int) -> int:
    """
    Clear the bit at position i in num
    """
    return num & ~(1 << i)

def clear_bits_through_i(num: int, i: int) -> int:
    """
    Clear bits from most significant to i
    """
    mask = (1 << i) - 1
    return mask & num

def clear_bits_through_0(num: int, i: int) -> int:
    """
    Clear bits from i to index 0
    """
    mask = (~0) << (i+1)
    return num & mask

def update_bit(num: int, i: int, bit_is_1: bool) -> int:
    """
    Update the bit at position i to either 1 or 0
    """
    value = 1 if bit_is_1 else 0
    mask = ~(1 << i)
    return num & mask | value << i

if __name__ == '__main__':
    vals = [(8, 3), (8, 1), (3, 0), (3, 1), (3, 2), (5, 0), (5, 1), (5, 2), (5, 3)]
    for num, i in vals:
        val = get_bit(num, i)
        print('bit at position {} in {} is 1? {}'.format(i, num, val))

    vals = [(1, 2)]
    for num, i in vals:
        val = set_bit(num, i)
        print('setting bit at position {} changes {} to {}'.format(i, num, val))

    vals = [(5, 2)]
    for num, i in vals:
        val = clear_bit(num, i)
        print('clearing bit at position {} changes {} to {}'.format(i, num, val))

    vals = [(13, 3), (13, 2)]
    for num, i in vals:
        val = clear_bits_through_i(num, i)
        print('clearing bits from most signifant to index {} changes {} to {}'.format(i, num, val))

    vals = [(13, 2), (13, 3)]
    for num, i in vals:
        val = clear_bits_through_0(num, i)
        print('clearing bits from index {} to least significant changes {} to {}'.format(i, num, val))

    vals = [(0, 0, True), (1, 0, False)]
    for num, i, b in vals:
        val = update_bit(num, i, b)
        print('setting bit at index {} to {} changes {} to {}'.format(i, b, num, val))
