# MEAN
def mean(x):
    'Compute arithmetic mean of an iterable'
    return sum(x) / len(x)

# FLOATABLE
def floatable(s):
    'Determine if an object can be converted to type float'
    try: float(s)
    except ValueError: return False
    return True

# DIST
def dist(p, q):
    'return 1 dimensional Euclidean distance'
    return abs(p - q)

# ASSIGN CLUSTERS
def assignClusters(data, clusters, centroids, point_assignments):
    'Assign each data point to the cluster with the nearest centroid, updating point assignments and clusters'
    for index1, value1 in enumerate(data):
        minDistance = 1000 # initialize minDistance to a large number to make we don't skip the if statement
        for index2, value2 in enumerate(centroids):
            if minDistance > dist(data[index1], centroids[index2]):
                minDistance = dist(data[index1], centroids[index2])
                closest_index = index2
        point_assignments[data[index1]] = centroids[closest_index]
        clusters[closest_index].append(data[index1])

# UPDATE CENTROIDS
def updateCentroids(clusters, centroids):
    'Update centroid values to the arithmetic mean of the values in each cluster'
    for index, value in enumerate(clusters):
        centroids[index] = mean(clusters[index])
