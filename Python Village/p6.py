"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 6 – Dictionaries

This program counts the frequency of a word in a string

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are
        separated by spaces. Words are case-sensitive, and the lines
        in the output can be in any order.
"""

Problem = 6

# @Note: no specific input format

# Read in the data from the input file
file = open(f"input/rosalind_ini{Problem}.txt", 'r')
dataset = file.read()

# Parse the data
words = dataset.split()

frequency_dict = {} # word -> frequency
for word in words:
    if word not in frequency_dict:
        frequency_dict[word] = 1
    else:
        frequency_dict[word] += 1

output = []
for word in frequency_dict:
    freq = frequency_dict[word]
    output.append(f"{word} {freq}\n")


file = open("p6.txt", 'w')
file.writelines(output)
