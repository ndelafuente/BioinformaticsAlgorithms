"""
Authors:
    Nicolas de la Fuente (ndelafuente@sandiego.edu)
    Jane Kim
    Danny Rosales
BA8A: Implement FarthestFirstTraversal

"""

ID = "ba8a-2"

# @Note: input format
# k m
# Data_0
# Data_1
# ...
# Data_k



# Read in the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
input = file.read()

# Parse the dataset
input = input.splitlines()
header = input[0].split()
k = int(header[0])  # number of clusters
m = int(header[1])  # the dimension

Data = [] # list of Data
for point in input[1: ]:
    point = [float(coord) for coord in point.split()] # "0.0 0.0" -> [0.0, 0.0]
    Data.append(point)


def EuclideanDistance(v, w, m):
    """
    Calculate the length of the line between points v and m

    @param v The first point
    @param w The second point
    @param m The m of the points

    @return The euclidean distance between the two points
    """
    sum = 0
    for i in range(m):
        sum += (v[i] - w[i]) ** 2

    return sum ** 0.5


Centers = []
rand_point = Data[0]
Centers.append(rand_point)

while len(Centers) < k:
    # Find the furthest point away from the centers
    max = -1
    Center = []
    for DataPoint in Data:
        # Calculate the shortest distance to any of the centers
        dist_list = []
        for x in Centers:
            dist = EuclideanDistance(DataPoint, x, m)
            dist_list.append(dist)
        
        min_dist = min(dist_list)


        if min_dist > max:
            max = min_dist
            Center = DataPoint


    Centers.append(Center)



for Center in Centers:
    print(*Center, sep=' ')