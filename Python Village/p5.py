"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 5 – Working with Files

This program reads an input file and writes each even-numbered line
(the first line in the file is 1) to an output file 

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the
        original file. Assume 1-based numbering of lines.
"""

Problem = 5

# @Note: no specific input format

# Read in the data from the input file
file = open(f"input/rosalind_ini{Problem}.txt", 'r')
dataset = file.read()

# Parse the data
dataset = dataset.splitlines()
even_lines = dataset[1 : : 2] # access every other element
output = "\n".join(even_lines)

file = open("p5.txt", 'w')
file.write(output)
