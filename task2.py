#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 84.8230016469

import math

data= input("Enter radius of sphere")
r= data
r= float(r)
part1= (4/3)*math.pi
volume= (part1*(pow(r,3)))
answer= float(volume)

# convert data into an integer. part1 = (4/3)*math.pi
# answer= (part1*(pow(r,3)))

#answer ---> float
#Then print

print("The volume=")
print(answer)
