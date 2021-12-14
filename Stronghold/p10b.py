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

# Read in the data from the input file
file = open("input/rosalind_gc.txt", 'r')
dataset = file.read()

# Parse the dataset
data = dataset.splitlines()

dna_dict = {}
current_ID = ""
for line in data:
    if line[0] == '>':
        # line is ID
        current_ID = line[1:]
        dna_dict[current_ID] = "" # initialize the entry
    else:
        # line is DNA string
        # print(f'dna_dict[{current_ID}] = "{dna_dict[current_ID]}"')
        dna_dict[current_ID] += line

# Initialize the variables
max_gc_content_id = "gobblety-gook"
max_gc_content = -1

for ID in dna_dict:
    dna_string = dna_dict[ID]

    # Count your Gs and Cs
    gc_count = 0
    for nt in dna_string:
        if nt == 'G' or nt == 'C':
            gc_count += 1
    
    dna_str_len = len(dna_string)

    # Calculate the GC content
    gc_content = (gc_count / dna_str_len) * 100

    # Check if we have reached a new record!
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_content_id = ID


print(max_gc_content_id)
print(max_gc_content)