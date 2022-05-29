# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:38:05 2022

@author: franc
"""

# Asumptions
# 1. Los nodos pueden utilizarse en cualquier dirección
# 2. Un tren sin color puede pasar por estaciones con color

import copy
import itertools
import click
import json

# The best way to solve this, is to make a map of each color

class Mapa:
    # A utily function to find the matrix, defined by train color,
    # that goes in the djikstra algorithm
    def mapear(self, b_network, color=""):
        # If this node is not of the same color as the train, then its path nodes
        # are added to its nodes (as long as they are not already there), then this
        # node is deleted from the path and from the network
        self.b_network = copy.deepcopy(b_network)
        for node in self.b_network:
            if self.b_network[node]["color"]:
                if self.b_network[node]["color"]!=color and color:
                    # Its not of the same color as the train
                    for node_path in self.b_network[node]['path']:
                        # print(node_path)
                        for node_conected in self.b_network[node]['path']:
                            if node_path != node_conected:
                                self.b_network[node_path]['path'].append(node_conected)
                                self.b_network[node_path]['path'].remove(node)
        
        if color:
            networkUsable = {nodo: value for nodo, value in
                                     self.b_network.items() if
                                     not value['color'] or
                                     value['color'] == color}
        # No nodes need to be deleted
        else:
            networkUsable = self.b_network
        translateDict = { nodo:idx for idx,nodo in enumerate(networkUsable) }
        
        # After every non usable node is deleted, we create the matrix map
        dimension = len(networkUsable)
        matrix = [[0 for col in range(dimension)] for row in range(dimension)]
        for nodo in networkUsable:
            idx_nodo = translateDict[nodo]
            for nodo_path in networkUsable[nodo]['path']:
                idx_siguiente = translateDict[nodo_path]
                matrix[idx_nodo][idx_siguiente]=1
        return matrix, translateDict


# Este problema lo podemos solucionar con djikstra
 
#Class to represent a graph
class Graph:
 
    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self,dist,queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1
         
        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
 
    # Function to print shortest path
    # from source to j
    # using parent array
    def printPath(self, parent, j):
        self.result = []
        #Base Case : If j is source
        
        if parent[j] == -1 :
            self.result.append(self.translateDict[j])
            return
        self.printPath(parent , parent[j])
        self.result.append(self.translateDict[j])
        
 
    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent, nodo):
        self.nodo = nodo
        self.printPath(parent,self.nodo)
 
    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''
    
    
    
    def dijkstra(self, graph, src, translateDict, nodo):
        self.translateDict = translateDict
        self.nodo = nodo
        self.src = src
        row = len(graph)
        col = len(graph[0])
 
        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row
 
        #Parent array to store
        # shortest path tree
        parents = [[-1] for col in range(row)]
        
        # alternate parents
 
        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0
     
        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
             
        #Find shortest path for all vertices
        follow = True
        while queue and follow:
 
            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)
 
            # remove min element    
            queue.remove(u)
 
            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            

            
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] == dist[i]:
                        # Hay otro camino óptimo con la misma distancia
                        if parents[i][0] == -1:
                            parents[i][0] = u                            
                        else: parents[i].append(u)
                    if dist[u] + graph[u][i] < dist[i]:
                        # Camino óptimo
                        dist[i] = dist[u] + graph[u][i]
                        if parents[i][0] == -1:
                            parents[i][0] = u
        vectores = list(itertools.product(*parents))
        results = []
        for parent3 in vectores:
            self.printSolution(dist,parent3, self.nodo)
            if self.result not in results:
                results.append(self.result)
        return results
        
    

# Click is a Python package for creating beautiful command line interfaces
# in a composable way with as little code as necessary.
@click.command()
@click.option('--filename', default='', help='Network file, in json format [required]')
@click.option('--origin', help='Source node of the network', required = True)
@click.option('--destination', help='Destination node of the network', required = True)
@click.option('--color', default='green', help='Train color, green, red [dont add for colorless]')


def runShortPath(filename, origin, destination, color):
    if not filename:
        click.echo('No file inserted, please insert a file')
        quit()
    else:
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
        except:
            click.echo('File not found, or not a json file')
            quit()
    if color:
        if color not in ['red', 'green']:
            click.echo("That color is not defined")
            quit()
    if not origin in data or not destination in data:
        click.echo("Destination or Origin node dosen't exist in the network")
        quit()
    
    if data[origin]['color'] or data[destination]['color']:
        if data[origin]['color'] != color or data[destination]['color'] != color:
            click.echo("The origin and the destination node must have the same color as the train")
            quit()
    
    m = Mapa()
    matrix, translateDict = m.mapear(data,color)

    
    origin_int = translateDict[origin]
    destination_int = translateDict[destination]
    
    g = Graph()
    inverseTranslateDict = {v: k for k, v in translateDict.items()}
    print(g.dijkstra(matrix, origin_int, inverseTranslateDict, destination_int))
if __name__ == '__main__':
    runShortPath()
