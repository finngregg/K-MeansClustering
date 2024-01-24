'''
K-Means Clustering
FNNGRE002
'''

import math
from statistics import mean

# Creates a class with attributes relating to a singular data point
# Point id, x co-ordinate, y co-ordinate, which cluster it belongs to and its distances to all three centroids
class point:
    def __init__(self, id, x, y, cluster_id):
        self.id = id
        self.x = x 
        self.y = y 
        self.cluster_id = cluster_id
        self.distances = [0,0,0]

# Finds the euclidean distance from each point to all 3 centroids and stores them within the point's "distances" attribute
def find_distances(points:list, centroids:list):
    for i in range(len(points)):
        for j in range(len(centroids)):
            p = points[i]
            c = centroids[j]
            p.distances[j] = math.dist([p.x,p.y], [c.x, c.y])

# Finds the minimum distance from a point to a centroid and assigns that point to that cluster 
def set_cluster(points:list):
    for i in range(len(points)):
        p = points[i]
        curr = p.distances.index(min(p.distances))+1
        p.cluster_id = curr

# Takes all points associated with a cluster and finds the new mean co-ordinate and assigns it to the centroid of the cluster
def set_mean(points:list,centroids:list, conv:list):
    for i in range(len(centroids)):
        cluster_x = []
        cluster_y = []
        for j in range(len(points)):
            p = points[j]
            if (p.cluster_id == i+1):
                cluster_x.append(p.x)
                cluster_y.append(p.y)
        
        mean_x = round(mean(cluster_x),1)
        mean_y = round(mean(cluster_y),1)
        # Checks for convergence, i.e. if the previous means are the same as the new ones, cluster has converged
        if (centroids[i].x == mean_x and centroids[i].y == mean_y):
           conv[i] = True
        else:
            centroids[i].x = mean_x
            centroids[i].y = mean_y

# Creates lists for each cluster containing the id numbers of the points assigned to that cluster
def make_clusters(points:list, clusters:dict):
    c1 = []
    c2 = []
    c3 = []
    for i in range(len(points)):
        p = points[i]
        if (p.cluster_id == 1):
            c1.append(p.id)
        if (p.cluster_id == 2):
            c2.append(p.id)
        if (p.cluster_id == 3):
            c3.append(p.id) 
    clusters[1] = c1
    clusters[2] = c2
    clusters[3] = c3

def main():
    # Creating datapoints from the list of 8 example coordinates
    points = [point(1,2,10,1), point(2,2,5,1), point(3,8,4,1), point(4,5,8,2), point(5,7,5,2),  point(6,6,4,2), point(7,1,2,3), point(8,4,9,3)]
    
    # Creating the inital centroids
    centroids = [point(9,2,10,1), point(10,5,8,2), point(11,1,2,3)]

    # Boolean to check convergence
    conv = [False, False, False]

    it = 1
    # Creates and opens ouput text file with writing privleges
    f= open("output.txt","w+")
    # Infinite loop
    while("GF"):
        # Checks to see whether the clusters have converged and breaks loops if they have
        if (conv[0] and conv[1] and conv[2]):
            break
        # Create dictionary of clusters
        clusters = { i:[] for i in range(1, 4) }
        make_clusters(points,clusters)
        find_distances(points, centroids)
        set_cluster(points)
        set_mean(points,centroids,conv)
        f.write(f"Iteration {it}\n")
        f.write("\n")
        for i in range(len(centroids)):
            out = ""
            for j in range(len(clusters[i+1])):
                out += str(clusters[i+1][j]) + " "
            f.write(f"Cluster {centroids[i].cluster_id}: {out}\n")
            f.write(f"Centroid: ({centroids[i].x},{centroids[i].y})\n")
            f.write("\n")
        it += 1
    # Closes output text file
    f.close() 
    
if __name__ == "__main__":
    main()