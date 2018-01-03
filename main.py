# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:16:51 2017

@author: hymzoque
"""

import timeit

import Initer
import Group

def ACO(dataset):
    initer = Initer.Initer(dataset)
    distances = initer.distances
    if (dataset == 52):
        g = Group.Group(distances, 0.4, 0, 100, 60, 2)
    elif (dataset == 130):
        g = Group.Group(distances, 0.4, 0, 200, 100, 2)
    
    with open("log_aco_" + str(dataset), "a") as f:
        best = g.evolution(file=f)
        best.drawout(initer.points, dataset)
        best.writein(f)
        f.write("\n")

def ACO_benchline(dataset):
    initer = Initer.Initer(dataset)
    distances = initer.distances
    if (dataset == 52):
        g = Group.Group(distances, 0.4, 0, 200, 300, None)
#    elif (dataset == 130):
#        g = Group.Group(distances, 0.2, 0, 300, 300, None)
    
    with open("log_benchline_" + str(dataset), "a") as f:
        best = g.evolution_benchline(file=f)
        best.drawout(initer.points, dataset)
        best.writein(f)
        f.write("\n")
        
def test_ACO(dataset):
    open("log_aco_" + str(dataset), "w").close()
    
    t1 = timeit.Timer("ACO(" + str(dataset) + ")", "from main import ACO")
    for i in range(10):
        time = t1.timeit(number=1)
        with open("log_aco_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")
        
def test_ACO_benchline(dataset):
    open("log_benchline_" + str(dataset), "w").close()
    
    t1 = timeit.Timer("ACO_benchline(" + str(dataset) + ")", "from main import ACO_benchline")
    for i in range(5):
        time = t1.timeit(number=1)
        with open("log_benchline_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")  

#ACO(52)
#ACO_benchline(52)
#test_ACO(52)
#test_ACO_benchline(52)
            
            