"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 16 - Construct the De Bruijn Graph of a String

Given a genome Text, PathGraphk(Text) is the path consisting of
|Text| - k + 1 edges, where the i-th edge of this path is labeled by
the i-th k-mer in Text and the i-th node of the path is labeled by
the i-th (k - 1)-mer in Text. The de Bruijn graph DeBruijn_k(Text)
is formed by gluing identically labeled nodes in PathGraph_k(Text).

Construct the de Bruijn graph of a string.

Given: An integer k and a string Text.

Return:DeBruijn_k(Text), in the form of an adjacency list.
"""

ID = "ba3d"

# @Note: input format
# k
# Text

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
dataset = file.read()

# Parse the dataset
dataset = dataset.splitlines()
k = int(dataset[0]) # convert k to an integer
text = dataset[1]

# Create the de Bruijn graph
num_edges = len(text) - k + 1 # number of edges on the graph
graph = {} # an empty dictionary
for i in range(num_edges):
    # Isolate the kmer from the rest of the string
    kmer = text[i: i + k]

    # Get the prefix and suffix for the kmer
    prefix = kmer[ : -1]
    suffix = kmer[1:   ]

    # If the prefix has not been added yet
    if prefix not in graph:
        graph[prefix] = [] # initialize an empty list to store suffixes
    
    graph[prefix].append(suffix) # add the suffix to the list

# Print the output in the form of an adjacency list
for prefix, suffixes in graph.items():
    suffix_str = ','.join(suffixes)
    print(prefix, '->', suffix_str)
