"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 3 – Strings and Lists

This program calculates generates a two-word phrase based on a string
and two pairs of start and stop indices.

Given: A string s of length at most 200 letters and 4 integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d
        (with space in between), inclusively. In other words, we should
        include elements s[b] and s[d] in our slice.
"""

Problem = 3

# @Note: input format
# s
# a b c d

# Read in the data from the input file
file = open(f"input/rosalind_ini{Problem}.txt", 'r')
dataset = file.read()

# Parse the data
dataset = dataset.splitlines()
(s, indices) = dataset
(a, b, c, d) = [int(x) for x in indices.split(' ')]

# Splice out the two words
first_word = s[a: b + 1]
second_word = s[c: d + 1]

# Concatenate the words with a space between them
selected_phrase = first_word + ' ' + second_word

print(selected_phrase)

