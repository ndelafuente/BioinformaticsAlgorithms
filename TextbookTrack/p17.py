"""
Author: Nicolas de la Fuente (ndelafuente@sandiego.edu)
GENG 430: Problem 17 - Construct the De Bruijn Graph of a Collection of k-mers

Given an arbitrary collection of k-mers Patterns (where some k-mers may appear
multiple times), we define CompositionGraph(Patterns) as a graph with |Patterns|
isolated edges. Every edge is labeled by a k-mer from Patterns, and the starting
and ending nodes of an edge are labeled by the prefix and suffix of the k-mer
labeling that edge. We then define the de Bruijn graph of Patterns, denoted 
DeBruijn(Patterns), by gluing identically labeled nodes in
CompositionGraph(Patterns), which yields the following algorithm.

    DEBRUIJN(Patterns)
        1. represent every k-mer in Patterns as an isolated edge between its prefix and suffix
        2. glue all nodes with identical labels, yielding the graph DeBruijn(Patterns)
        3. return DeBruijn(Patterns)

Construct the de Bruijn graph from a collection of k-mers.

Given: A collection of k-mers Patterns.

Return: The de Bruijn graph DeBruijn(Patterns),
        in the form of an adjacency list.

"""

ID = "ba3e"

# @Note: input format
# kmer (on each line)

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')

# Parse the dataset
dataset = file.read().strip().split()


# Construct the de Bruijn graph
graph = {} # a dict for the de Bruijn graph
for kmer in dataset:
    # Get the prefix and suffix of the kmer
    prefix = kmer[ : -1]
    suffix = kmer[1:   ]

    if prefix not in graph: # if the prefix hasn't been added
        graph[prefix] =  '-> ' + suffix # add an entry with the suffix
    else: # if the prefix has already been added
        graph[prefix] += ',' + suffix # append the suffix to the entry


# Print output
out = open(f"output_{ID}.txt", 'w')
for key, value in graph.items():
    print(key, value, file = out)