#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

import math

a= input("Enter 'a' variable")
b= input("Enter 'b' variable")
c= input("Enter 'c' variabe")

a= int(a)
b= int(b)
c= int(c)

part1= (c-b)
x= (part1/a)

print("x=")
print(x)
