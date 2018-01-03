# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:45:26 2017

@author: hymzoque
"""

import Pheromone
import Ant
import random
import math

class Group:
    
    def __init__(self, distances, evaporation_rate, init_phero, ant_num, loop_time, beta):
        self.__distances = distances
        self.__evaporation_rate = evaporation_rate
        self.__ant_num = ant_num
        self.__loop_time = loop_time
        self.__pheromone = Pheromone.Pheromone(len(distances), init_phero)
        self.__beta = beta
    
    def evolution(self, doprint=1, file=None):
        best = None
        for time in range(self.__loop_time):
            self.__group = []
            # new ant generation
            # first time
            if (time == 0):
                for index in range(self.__ant_num):
                    self.__group.append(Ant.random_ant(self.__distances))
            else:
                # calculate pheromone probability table
                length = self.__pheromone.size
                phe_table = self.__pheromone.pheromone
                phe_pro_table = self.__phe_pro_table(length, phe_table)
                for index in range(self.__ant_num):
                    self.__group.append(self.__ant_find_way(phe_pro_table))
            # select best
            local_best = max(self.__group)
            if (best == None or local_best.distance < best.distance):
                best = local_best
            # produce pheromone
            for ant in self.__group:
                self.__pheromone.produce(ant)
            # evaporation
            self.__pheromone.evaporation(self.__evaporation_rate)
            
            if (doprint):
                print("-" + str(time) + "-:" + str(best.distance))
            if (file != None):
                file.write("-")
                file.write(str(time))
                file.write("-:")
                file.write(str(best.distance))
                file.write("\n")
                
        return best
    
    def evolution_benchline(self, doprint=1, file=None):
        best = None
        for time in range(self.__loop_time):
            self.__group = []
            # new ant generation
            # first time
            if (time == 0):
                for index in range(self.__ant_num):
                    self.__group.append(Ant.random_ant(self.__distances))
            else:
                # calculate pheromone probability table
                length = self.__pheromone.size
                phe_table = self.__pheromone.pheromone
                phe_pro_table = self.__phe_pro_table_benchline(length, phe_table)
                for index in range(self.__ant_num):
                    self.__group.append(self.__ant_find_way_benchline(phe_pro_table))
            # select best
            local_best = max(self.__group)
            if (best == None or local_best.distance < best.distance):
                best = local_best
            # produce pheromone
            for ant in self.__group:
                self.__pheromone.produce(ant)
            # evaporation
            self.__pheromone.evaporation(self.__evaporation_rate)
            
            if (doprint):
                print("-" + str(time) + "-:" + str(best.distance))
            if (file != None):
                file.write("-")
                file.write(str(time))
                file.write("-:")
                file.write(str(best.distance))
                file.write("\n")
            
        return best
    
    # calculate pheromone probability table
    def __phe_pro_table_benchline(self, length, phe_table):
        return phe_table
    
    # calculate pheromone probability table
    def __phe_pro_table(self, length, phe_table):
        phe_pro_table = []
        for p1 in range(length):
            temp = []
            for p2 in range(p1):
                temp.append(phe_table[p1][p2] / math.pow(self.__distances[p1][p2], self.__beta))
            phe_pro_table.append(temp)
        return phe_pro_table
    
    # produce new ant by the pheromone
    def __ant_find_way(self, phe_pro_table):
        length = self.__pheromone.size
        
        path_temp = list(range(length))
        begin = random.randint(0, length - 1)
        path = [begin]
        path_temp.remove(begin)
        
        for i in range(length - 1):
            self.__choose_next(path_temp, path, phe_pro_table)
        
        return Ant.Ant(path, self.__distances)

    # by the pheromone
    def __choose_next(self, path_temp, path, phe_pro_table):
        time = len(path_temp)
        for now in range(time):
            p1 = path[len(path) - 1]
            # path probability weight list
            path_pro_temp = []
            for p2 in path_temp:
                if (p1 > p2):
                    path_pro_temp.append(phe_pro_table[p1][p2])
                else:
                    path_pro_temp.append(phe_pro_table[p2][p1])
            pro_sum = sum(path_pro_temp)
            # random choose next point with weight
            ran = random.uniform(0, pro_sum)
            selection = None
            for index in range(len(path_pro_temp)):
                ran = ran - path_pro_temp[index]
                if (ran <= 0):
                    selection = path_temp[index]
                    break
            path_temp.remove(selection)
            path.append(selection)


    def __ant_find_way_benchline(self, phe_pro_table):
        length = self.__pheromone.size
        
        path_temp = list(range(length))
        begin = random.randint(0, length - 1)
        path = [begin]
        path_temp.remove(begin)
        
        for i in range(length - 1):
            self.__choose_next_benchline(path_temp, path, phe_pro_table)
        
        return Ant.Ant(path, self.__distances)    
       
    def __choose_next_benchline(self, path_temp, path, phe_pro_table):
        time = len(path_temp)
        for now in range(time):
            p1 = path[len(path) - 1]
            # path probability weight list
            path_pro_temp = []
            for p2 in path_temp:
                if (p1 > p2):
                    path_pro_temp.append(phe_pro_table[p1][p2])
                else:
                    path_pro_temp.append(phe_pro_table[p2][p1])
            pro_sum = sum(path_pro_temp)
            # random choose next point with weight
            ran = random.uniform(0, pro_sum)
            selection = None
            for index in range(len(path_pro_temp)):
                ran = ran - path_pro_temp[index]
                if (ran <= 0):
                    selection = path_temp[index]
                    break
            path_temp.remove(selection)
            path.append(selection)
        
        
    
    
    
    