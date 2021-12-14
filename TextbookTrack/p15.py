"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 15 - Construct the Overlap Graph of a Collection of k-mers

In this chapter, we use the terms prefix and suffix to refer to the first
k − 1 nucleotides and last k − 1 nucleotides of a k-mer, respectively.

Given an arbitrary collection of k-mers Patterns, we form a graph having a
node for each k-mer in Patterns and connect k-mers Pattern and Pattern' by
a directed edge if Suffix(Pattern) is equal to Prefix(Pattern'). The resulting
graph is called the overlap graph on these k-mers, denoted Overlap(Patterns).

Given: A collection Patterns of k-mers.

Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
"""

ID = "ba3c"

# @Note: input format
# Patterns (where each kmer is on a new line)

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
dataset = file.read()

# Parse the dataset
patterns = dataset.splitlines()

out = open(f"output_{ID}.txt", 'w') # output file
# For each pattern in the list
for i in range(len(patterns)): 
    suffix = patterns[i][1: ] # isolate the suffix
    # And go back over the list
    for j in range(len(patterns)):
        prefix = patterns[j][ : -1] # isolating the prefix
        # Print it out if the prefix and suffix match
        if i != j and suffix == prefix:
            print(patterns[i], patterns[j], sep = ' -> ', file = out)
