# A simple test case generator for CSC 349 at Cal Poly
# Outputs a file with a list of duplicates, except for one unique element
# Credit: Rodrigo Canaan 

import random
import datetime
import os.path
from os import path

# Parameters for the generator
min = -100
max = 100
n = 50

# Generate a random list of distinct numbers	
numbers = random.sample(range(min,max),n)

# Add singleton of the first number to the final list
unique = numbers[0]
L = [unique]

# Add duplicates of the remaining entries, then sort
for n in numbers[1:]:
	L.append(n)
	L.append(n)
L.sort()

# Write sorted list to file.
# File will be named "nique{n}", where n is the singleton entry
# If this file name already exists, the current datetime will be appended
name = "unique{}".format(unique)
if path.exists(name):
	now = datetime.datetime.now()
	name+=" {}".format(now)
with open(name,"x") as f:
	for n in L:
		f.write("{}\n".format(n))
f.close()
print("Wrote list to file {}".format(name))