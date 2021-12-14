"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 4 – Conditions and Loops

This program calculates takes two triangle side lengths a and b, and 
calculates the square of the hypotenuse (c^2)

Given: Two positive integers a and b (a < b < 10000 ).

Return: The sum of all odd integers from a through b, inclusively.
"""

Problem = 4

# @Note: input format
# a b

# Read in the data from the input file
file = open(f"input/rosalind_ini{Problem}.txt", 'r')
dataset = file.read()

# Parse the data
(a, b) = dataset.split()
a = int(a)
b = int(b)

# Ensure starting number is odd
a = a if a % 2 else a + 1

# Calculate the sum of each odd number up to and including b
total = sum(range(a, b + 1, 2))

print(total)
