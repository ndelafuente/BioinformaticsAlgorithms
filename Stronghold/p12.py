"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 12 – Finding a Motif in DNA

Given two strings s and t, t is a substring of s if t is contained as a contiguous
collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left,
including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG"
are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the first and
last positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG",
then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will
have multiple locations in s if it occurs more than once as a substring of s.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

Problem = 12

# @Note: input format
# s (sequence)
# t (subsequence)

# Read in the data from the input 
file = open("input/rosalind_subs.txt", 'r')
dataset = file.read()

# Parse the dataset
(sequence, subsequence) = dataset.splitlines()

motif_locations = [] # a list to store the morif locations
for i in range(len(sequence)):
    # Create a string of the same length of the subsequence
    a = sequence[i: i + len(subsequence)]
    # Add the start position of the string if it equals the subsequence
    if a == subsequence:
        motif_locations.append(str(i + 1))

print(' '.join(motif_locations))