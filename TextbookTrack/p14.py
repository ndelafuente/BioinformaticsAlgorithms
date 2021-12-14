"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 14 - Reconstruct a String from its Genome Path

Find the string spelled by a genome path.

Given: A sequence of k-mers Pattern_1, ... , Pattern_n such that the
last k - 1 symbols of Pattern_i are equal to the first k - 1 symbols
of Pattern_i+1 for i from 1 to n - 1.

Return: A string Text of length k + n - 1 where the i-th k-mer in Text
is equal to Pattern_i for all i.
"""

ID = "ba3b"

# @Note: input format
# Pattern_1
# ...
# Pattern_n

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
dataset = file.read()

# Parse the dataset
patterns = dataset.splitlines()

# Reconstruct the sequence
sequence = patterns[0] # get the first pattern
for pattern in patterns[1: ]: # for the rest of the patterns
    sequence += pattern[-1] # add the last character to the sequence

print(sequence) # print the sequence