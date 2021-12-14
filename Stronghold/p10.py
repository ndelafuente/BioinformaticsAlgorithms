"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 10 – Computing GC Content

The GC-content of a DNA string is given by the percentage of symbols in the
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database.
A commonly used method of string labeling is called FASTA format. In this
format, the string is introduced by a line that begins with '>', followed
by some labeling information. Subsequent lines contain the string itself;
the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return:
The ID of the string having the highest GC-content, followed by the GC-content
of that string. Rosalind allows for a default error of 0.001 in all decimal
answers unless otherwise stated; please see the note on absolute error below.
"""

Problem = 10

# @Note: input format
# >id
# dna_string (any number of lines)
# (^ repeated up to 10 times)

ID_LEN = 13

# Read in the data from the input file
file = open("input/rosalind_gc.txt", 'r')
dataset = file.read().splitlines()

# Parse the dataset
data = "".join(dataset)[1: ].split('>')

# Reformat the data into a dictionary that maps the ID to the DNA string
dna_dict = {line[0 :ID_LEN]: line[ID_LEN: ] for line in data}

# Define the calculation for GC content
def gc_content(dna_string):
    gc_count = dna_string.count('G') + dna_string.count('C')
    return (gc_count / len(dna_string)) * 100

# Create a dictionary mapping GC content to the DNA string ID
gc_content_dict = {gc_content(dna_str): id for (id, dna_str) in dna_dict.items()}

# Find the DNA string with the maximum GC content
max_gc_content = max(gc_content_dict.keys())
max_gc_content_id = gc_content_dict[max_gc_content]

# Print the outpu
print(max_gc_content_id)
print(max_gc_content)



