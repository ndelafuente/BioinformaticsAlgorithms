"""
Authors:
    Nicolas de la Fuente (ndelafuente@sandiego.edu)
    Jane Kim
    Danny Rosales
BA8A: Implement FarthestFirstTraversal

"""

import random

ID = "ba8a-2"

# @Note: input format
# k m
# Data_0
# Data_1
# ...
# Data_k

# Read in the data from the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
dataset = file.read()

# Parse the dataset
dataset = dataset.splitlines()
header = dataset[0].split()
num_clusters = int(header[0])   # k
dimension = int(header[1])      # m

points = [] # list of points
for point in dataset[1: ]:
    point = [float(coord) for coord in point.split()] # "0.0 0.0" -> [0.0, 0.0]
    points.append(point)

def EuclideanDistance(v, w):
    """
    Calculate the length of the line between points v and m

    @param v The first point
    @param w The second point
    @param m The dimension of the points

    @return The euclidean distance between the two points
    """
    m = len(v)
    sum = 0
    for i in range(m):
        sum += (v[i] - w[i]) ** 2

    return sum ** 0.5

def MinDistance(DataPoint, Centers):
    min = EuclideanDistance(DataPoint, Centers[0])
    for x in Centers[: ]:
        dist = EuclideanDistance(DataPoint, x)
        # print("      x:", x, "-> dist:", dist)
        if dist < min:
            min = dist
    return min

def MaxMinDistance(Data, Centers):
    max = -1
    Center = Data[0]
    for DataPoint in Data:
        # print("   DataPoint:", DataPoint)
        min_dist = MinDistance(DataPoint, Centers)
        # print("   min_dist:", min_dist, "max", max, Center)
        if min_dist > max:
            max = min_dist
            Center = DataPoint
    return Center


def FarthestFirstTraversal(Data, k):
    Centers = []
    rand_point = Data[0]
    # rand_point = random.choice(Data) # choose a random element from Data
    Centers.append(rand_point)
    # print("Adding", rand_point)
    while len(Centers) < k:
        DataPoint = MaxMinDistance(Data, Centers)
        # print("Adding", DataPoint)
        Centers.append(DataPoint)
    
    return Centers


Centers = FarthestFirstTraversal(points, num_clusters)
for Center in Centers:
    print(*Center, sep=' ')