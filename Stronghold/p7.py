"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 7 – Counting DNA Nucleotides

A string is simply an ordered collection of symbols selected from some
alphabet and formed into a word; the length of a string is the number
of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the
symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nucleotides.

Return: Four integers (separated by spaces) counting the respective
    number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

Problem = 7

# @Note: input format
# s (a string containing any number A, C, T, or G)

# Read in the data from the input file
file = open("input/rosalind_dna.txt", 'r')
dataset = file.readline()

# Parse the data
A_count = dataset.count('A')
C_count = dataset.count('C')
G_count = dataset.count('G')
T_count = dataset.count('T')

print(A_count, C_count, G_count, T_count)
