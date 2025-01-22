def classical_xor(control_bit, target_bit):
    return target_bit ^ (control_bit & 1)

# call xor for all input cases
print("Truth Table for Controlled-NOT:")
print("Control Target  Result")
print("------- ------  ------")
for control in [0, 1]:
    for target in [0, 1]:
        result = classical_xor(control, target)
        print(f"   {control}      {target}       {result}")
