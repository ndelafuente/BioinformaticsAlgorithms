"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
Reconstruct a String from its k-mer Composition

solved by 583

Reconstruct a string from its k-mer composition.

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns.
(If multiple answers exist, you may return any one.)
"""

ID = "BA3H"

# @Note: input format
# 
# kmer (on each line)

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')

# Parse the dataset
dataset = file.read().strip().split()


graph = {} # a dict for the debrujin graph
for kmer in dataset:
    prefix = item[ : -1]
    suffix = item[1:   ]
    if prefix not in graph:
        graph[prefix] = '-> ' + suffix + ' '
    else:
        graph[prefix] += ',' + suffix


# Print output
for key, value in graph.items()
    print(key, value)