# README for CSC3022F Assignment 4

## clustering.py
clustering.py implements an algorithm which is capable of categorizing the provided datapoints into k groups of similarity. 
This file contains both the "point" class of this assignment, the methods required for implementing k-means clustering and the main method. 

* Classes 
```python
    class point:
```
* Methods
```python
    def find_distances(points:list, centroids:list):
    def set_cluster(points:list):
    def set_mean(points:list,centroids:list, conv:list):
    def make_clusters(points:list, clusters:dict):
    def main():
```

## Makefile
The Makefile builds a working python virtual environment from scratch. 

Some examples have been commented out in the Makfile. The main commands include:
* make - creates virtual environment
* make clean - removes virtual environment