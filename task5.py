#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math

volume= input("What is the volume of the sphere?")

volume= float(volume)

part1= (math.pi*(4/3))
part1= float(part1)

part2= (volume/part1)
part2= float(part2)

answer= (part2**(1/3))
# answer= (pow(part2,(1/3))

print("The radius is=")
print(answer)
