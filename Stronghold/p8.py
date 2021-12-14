"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 8 – Transcribing DNA into RNA

An RNA string is a string formed from the alphabet containing A, C, G, and U.

Given a DNA string t corresponding to a coding strand, its transcribed RNA
string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

Problem = 8

# @Note: input format
# t

# Read in the data from the input file
file = open("input/rosalind_rna.txt", 'r')
dataset = file.readline()

# Parse the data
dna_string = dataset
rna_string = dna_string.replace('T', 'U')

print(rna_string)
