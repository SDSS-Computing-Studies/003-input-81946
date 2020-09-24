#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

import math

a= input("What is the length of one short side?")
b= input("What is the other short side length")

a= int(a)
b= int(b)

part1= pow(a,2)
part2= pow(b,2)

c= (part1 + part2)

c= int(c)

answer= math.sqrt(c)

print("The hypotenuse is=")
print(answer)
