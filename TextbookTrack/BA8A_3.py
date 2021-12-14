"""
Authors:
    Nicolas de la Fuente (ndelafuente@sandiego.edu)
    Jane Kim
    Danny Rosales
BA8A: Implement FarthestFirstTraversal

"""

def FarthestFirstTraversal(data, k, m):
    """
    A clustering algorithm

    @param data - The list of points
    @param k - The number of centers to find
    @param m - The dimension of the points

    @return A list of centers
    """

    # Subroutine definition
    def EuclideanDistance(v, w):
        """
        Calculate the length of the line between points v and m

        @param v The first point
        @param w The second point

        @return The euclidean distance between the two points
        """
        sum = 0
        for i in range(m):
            sum += (v[i] - w[i]) ** 2

        return sum ** 0.5
    
    def MinDistance(data_point, centers):
        """
        Calculate the minimum distance from a point to any of the centers

        @param data_point The data point
        @param centers The list of centers

        @return The shortest distance to a center
        """
        min_dist = EuclideanDistance(data_point, centers[0])
        for center in centers[1: ]:
            dist = EuclideanDistance(data_point, center)

            if dist < min_dist:
                min_dist = dist
        
        return min_dist

    def FarthestPoint(data, centers):
        """
        Find the farthest point in data from centers

        @param data The list of points
        @param centers The list of centers

        @return The data point farthest from any of the centers
        """
        max_dist = -1
        furthest_point = ()
        for data_point in data:
            min_dist = MinDistance(data_point, centers)

            if min_dist > max_dist:
                max_dist = min_dist
                furthest_point = data_point
        
        return furthest_point


    # Main routine
    centers = []
    rand_point = data[0]
    centers.append(rand_point)

    while len(centers) < k:
        # Find the furthest point away from the centers
        center = FarthestPoint(data, centers)

        # Add it to the list
        centers.append(center)
    
    return centers


# @Note: input format
# k m
# data_0
# data_1
# ...
# data_n

ID = "ba8a"

# Read in the input 
file = open(f"input/rosalind_{ID}.txt", 'r')
input = file.read()

# Parse the dataset
input = input.splitlines()
header = input[0].split()
k = int(header[0])  # number of clusters
m = int(header[1])  # the dimension of the points

data = [] # a list for the data points
for line in input[1: ]:
    # Convert each coordinate from a string to a float, then add them to a tuple
    point = tuple(float(coord) for coord in line.split())
    data.append(point)

# Find the centers using farthest first traversal
centers = FarthestFirstTraversal(data, k, m)

# Print the output
for center in centers:
    print(*center, sep=' ')