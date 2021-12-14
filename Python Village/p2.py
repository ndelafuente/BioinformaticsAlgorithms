"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 2 – Variables and Some Arithmetic

This program calculates takes two triangle side lengths a and b, and 
calculates the square of the hypotenuse (c^2)

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse
        of the right triangle whose legs have lengths a and b.
"""

Problem = 2

# @Note: input format
# a b

# Read in the data from the input file
file = open(f"input/rosalind_ini{Problem}.txt", 'r')
dataset = file.read()

# Parse the data
(a, b) = dataset.split()
a = int(a)
b = int(b)

# Calculate the square of the hypotenuse
c_squared = (a ** 2) + (b ** 2)

print(c_squared)

