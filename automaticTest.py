# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:01:24 2022

@author: franc
"""

import unittest
import pickle

# This are the classes we want to test. So, we need to import them
from shortPath import Mapa as MapaClass
from shortPath import Graph as GraphClass


# Importing a dictionary containing the demoNetwork for testing
with open("demoNetwork", "rb") as fp:   # Unpickling
    demoNetwork = pickle.load(fp)

# Importing lists containing expectedMatrix (for djikstra), translateDict
# (for translating the nodes to integer), expectedResult (shortest path result)
# items in each list are orederd by color: first is Colorless, 
# The second is red, ant the third is green

with open("expectedMatrix", "rb") as fp:   # Unpickling
    expectedMatrix = pickle.load(fp)

with open("translateDict", "rb") as fp:   # Unpickling
    translateDict = pickle.load(fp)

with open("expectedResult", "rb") as fp:   # Unpickling
    expectedResult = pickle.load(fp)

inverseTranslateDict = []
for i in translateDict:
    inverseTranslateDict.append({v: k for k, v in i.items()})

colors = ['', 'red', 'green']

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    m = MapaClass()  # instantiate the Person Class
    
    g = GraphClass()
    # test case function to check the mapear function
    def test_0_mapear(self):
        print("\nStart Mapa test\n")
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        # We will test the example data, to check if the output matches
        # the expected result
        
        # 1. Colorless train matrix
        # 2. Red train matrix
        # 3. Green train matrix
        for idx, color in enumerate(colors):
            self.matrix, self.translateDict = self.m.mapear(demoNetwork,color)
            self.assertListEqual(self.matrix, expectedMatrix[idx])

    
    def test_1_minDistance(self):
        print("\nStart minDistance test\n")
        dist = [0, 1, 2, 3, 4, float("Inf"), 3]
        queue = [4, 5, 6]
        expectedResult = 6
        result = self.g.minDistance(dist,queue)
        self.assertEqual(expectedResult, result)
    
    # test case function to check the Djikstra Algorithm
    def test_2_djikstra(self):
        origin_int,destination_int = 0,5
        # expectedResult = [['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'g', 'i', 'f']]
        print("\nStart djikstra test\n")
        """
        Any method that starts with ``test_`` will be considered as a test case.
        """
        
        for idx, color in enumerate(colors):
              self.result = self.g.dijkstra(expectedMatrix[idx],
                                      origin_int,
                                      inverseTranslateDict[idx],
                                      destination_int
                                      )
              self.assertListEqual(self.result, expectedResult[idx])



if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
