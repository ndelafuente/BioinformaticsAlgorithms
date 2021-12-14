"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 13 - Generate the k-mer Composition of a String

Given a string Text, its k-mer composition Compositionk(Text) is the
collection of all k-mer substrings of Text (including repeated k-mers).
For example,

    Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}

Note that we have listed k-mers in lexicographic order (i.e., how they
would appear in a dictionary) rather than in the order of their appearance
in TATGGGGTGC. We have done this because the correct ordering of the reads
is unknown when they are generated.

Generate the k-mer composition of a string.

Given: An integer k and a string Text.

Return: Composition_k(Text) (the k-mers can be provided in any order).
"""

ID = "ba3a"

# @Note: input format
# k
# text

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
dataset = file.read()

# Parse the dataset
dataset = dataset.splitlines()
k = int(dataset[0]) # convert k to an integer
text = dataset[1]

# Get the composition of the string
composition = [] # create an empty list
for i in range(len(text) - k + 1): # loop through the text up to the last full kmer
    kmer = text[i: i + k] # get the kmer from the text
    composition.append(kmer) # add the kmer to the composition

composition.sort() # sort the composition alphabetically

# print each kmer on a new line
out = open(f"output_{ID}.txt", 'w')
for kmer in composition:
    print(kmer, file = out)