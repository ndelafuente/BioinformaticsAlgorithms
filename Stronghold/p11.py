"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 11 – Counting Point Mutations

Given two strings s and t of equal length, the Hamming distance
between s and t, denoted dH(s,t), is the number of corresponding
symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

Problem = 11

# @Note: input format
# s
# t

# Read in the data from the input file
file = open("input/rosalind_hamm.txt", 'r')
dataset = file.read()

# Parse the dataset
(s, t) = dataset.splitlines()

hamming_distance = 0
for i in range(len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)