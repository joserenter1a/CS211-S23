"""
Binary Representation in Python
Author: Jose Renteria
Done for CS211 Class Encore

"""

"""
How to represent a binary number in Python
"""

one = 0b1
print(one)

two = 0b10
print(two)

three = one + two

print(f"{three} == {bin(three)}")
print(three is (one + two))

# use bin to convert to binary

print("-" * 50)
"""
Binary arithmetic
"""

print(bin(one | two))
# why is this three?

print(bin(one & two))
# why is this zero?

print("-" * 50)

"""
Bit shifting 
"""
bin_FF = 0b11111111

hex_FF = 0xFF
print(hex_FF == bin_FF)

print("Original binary value of 255")
print(bin(bin_FF))
print("Left shift binary value by 2")
print(bin(bin_FF << 2))
print("Right shift binary value by 4")
print(bin(bin_FF >> 4))

"""
Bit mask, let's say we want to extract the 4 leftmost bits of an 8bit binary number
"""
print("-" * 50)

mask = 0b11110000
bitnum = 0b10101100

extracted = (mask & bitnum) >> 4

print(bin(mask))
print(bin(bitnum))
print(bin(mask & bitnum))
print("By default Python will not include leading zeroes")
print(bin(extracted))
