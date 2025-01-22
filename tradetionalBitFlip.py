# define a helper method which applies NOT and masks the result, so we only pay attention to the final bit
def classical_not(bit):
    return ~bit & 1

# apply a bitwise NOT
bit_zero = 0
flipped_bit_zero = classical_not(bit_zero)
print(f"Original bit: {bit_zero}")
print(f"After NOT using ~: {flipped_bit_zero}")

bit_one = 1
flipped_bit_one = classical_not(bit_one)
print(f"Original bit: {bit_one}")
print(f"After NOT using ~: {flipped_bit_one}")