# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:13:03 2017

@author: hymzoque
"""

# each line segmant set a pheromone counter
class Pheromone:
    
    def __init__(self, size, init_phero):
        self.size = size
        self.__init_pheromone(init_phero)
        
    # init
    def __init_pheromone(self, init_phero):
        pheromone = []
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append(init_phero)
            pheromone.append(temp)
        self.pheromone = pheromone
    
    # evaporation
    # only update when p1 > p2, [p1][p2]
    def evaporation(self, rate):
        for p1 in range(self.size):
            for p2 in range(p1):
                self.pheromone[p1][p2] = self.pheromone[p1][p2] * (1 - rate)
    
    # produce pheromone
    # only update when p1 > p2, [p1][p2]
    def produce(self, ant):
        path = ant.path
        for index in range(self.size):
            p1 = path[index]
            p2 = path[index + 1 if index != self.size - 1 else 0]
            if (p1 < p2) :
                p1, p2 = p2, p1
            self.pheromone[p1][p2] += ant.pheromone
    
            
            
            