# Bit Manipulation

## The operators

There are 6 bitwise operators worth knowing for interviews:

1. Bitwise AND (&) - 1 if both bits are 1, else 0
2. Bitwise OR (|) - 1 if either bit is 1, else 0
3. Bitwise XOR (^) - 1 if two bits are different, else 0
4. Bitwise NOT (!) - 1 if 0, else 0
5. Left shift (<<) - shift all bits left by n places
6. Right shift (>>) - shift all bits right by n places

XOR is most useful in techical interviews.

## Bit facts

1s and 0s denotes a sequences of 1's and 0's respectively. It's important to work through examples of these rules to understand why they are true.

```bash
x ^ 0s = 0s
x ^ 1s = ~x
x ^ x = 0
x & 0s = 0
x & 1s = x
x & x = x
x | 0s = x
x | 1s = 1s
x | x = x
```

## Two's Complement and Negative Numbers

The final bit in a number is the sign bit. If 1, it's negative else positive.

Computers typically store negative numbers as 2's complement of it's absolute value. More formally:

The n-bit binary representation of negative K is concat(1, 2^(n-1) - K). The first 1 is the sign bit.

For example with 4 bit numbers:

```
-1 = concat(1, 2^(4-1) - 1) = concat(1, 7) = concat(1, 111) = 1111
```

A simpler way to do this is to take the positive value, invert all it's bits (~), then add 1.

For example with 4 bit numbers:

```
3 = 0011
-3 = concat(1, ~011 + 1) = concat(1, 100 + 1) = concat(1, 101) = 1101
```

## Arithmetic vs Logical Right Shift

Arithmetic right shift (>>) essentially divides by two. We shift all bits to the right and fill in new values with the sign bit.

For example:

```
(0)100 = 4
>>(0100, 1) = 0010 = 2

(1)100 = -4
>>(1100, 1) = 1110 = -2
```

In a logical right shift (>>>), we shift all bits to the right (including the sign bit) then set the sign bit to 0.

For example:

```
10110101 = -75
>>>(10110101, 1) = 01011010 = 90
```

Repeated logical right shifts on a negative number reduce a value to 0 because we are replacing the most significant bit with 0 repeatedly. 0s = 0.

Repeated arithmetic right shifts on a negative number reduce a value to -1 because we are replacing the most significant bit with the sign bit repeatedly. Signed integer sequence of 1s = -1.

## Common bit tasks - getting and setting

To determine whether the bit at position i is 1 in num, we move 1 to the left by i places then compare it to num with the AND operator. The AND operator clears all bits except those at position i. If the result is not zero, then the bit at position i must have been 1 (return True).

```python
# get bit
def get_bit(num: int, i: int) -> bool:
    """determine if the bit at position i in num is 1 or 0"""
    return (num & (1 << i)) != 0

# get_bit(8, 3) = True
# get_bit(8, 0) = False
```

To set a bit, move 1 i positions to the left. Then do a bitwise OR with num. This will only change the bit at position i.

```python
def set_bit(num: int, i: int) -> int:
    """
    Set the bit at position i in num to 1.
    """
    return num | (1 << i)
```

First we create a mask. We move 1 i positions left. Then invert all bits with NOT. Then we do an AND with num. Only the values at position ith position are cleared.

```python
def clear_bit(num: int, i: int) -> int:
    """
    Clear the bit at position i in num
    """
    return num & ~(1 << i)
```

Here we want to generate a mask which is a sequence of 0's followed by 1's.

```python
def clear_bits_through_i(num: int, i: int) -> int:
    """
    Clear bits from most significant to i
    """
    mask = (1 << i) - 1  # creates a mask of 00000011 for example
    return mask & num
```

Here we want to generate a mask which is a sequence of 1's followed by 0's.

```python
def clear_bits_through_0(num: int, i: int) -> int:
    """
    Clear bits from i to index 0
    """
    mask = (~0) << (i+1)
    return num & mask
```

First create a mask and use it to clear the bit at position i (eg 11101111 & num). Then we shift the intended value left by i bits. This will put the intended value at the intended position. Using OR we only change the value at position i (we know it's now 0 in the num).

```python
def update_bit(num: int, i: int, bit_is_1: bool) -> int:
    """
    Update the bit at position i to either 1 or 0
    """
    value = 1 if bit_is_1 else 0
    mask = ~(1 << i)
    return num & mask | value << i
```







