"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 9 – Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other,
as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s' formed by
reversing the symbols of s, then taking the complement of each symbol 
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s' of s.
"""

Problem = 9

# @Note: input format
# s

# Read in the data from the input file
file = open("input/rosalind_revc.txt", 'r')
dataset = file.readline().strip()

# Reverse the DNA string
dna_reversed = dataset[::-1]

# Create a dictionary to perform the switcheroohoohoo
switcheroo = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
}

# Perform switcheroohoohoo
reverse_complement = "".join([switcheroo[nt] for nt in dna_reversed])

print(reverse_complement)
