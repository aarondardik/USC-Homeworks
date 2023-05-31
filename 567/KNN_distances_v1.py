#script to compute distances repeatedly for finding minima in KNN

import numpy as np
import math 

def addClassChar(c, arr):
    if type(arr[len(arr) -1]) == str:
        return arr
    else:
        arr.append(c)
        return arr 

def removeClassChar(arr):
    if type(arr[len(arr)-1]) == str:
        arr.pop(len(arr)-1)
        return arr
    else:
        return arr

def distance(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i]-p2[i])*(p1[i]-p2[i])
    
    return math.sqrt(total)


def distance_from_each_in_list(p1, arr):
    classes = []
    for item in arr:
        if type(item[len(item)-1]) == str:
            classes.append(item[len(item)-1])
            item.pop(len(item)-1) 
    results = []
    for item in arr:
        results.append(distance(p1, item))
    
    return classes, results

#def distance_with_class(p1, arr):
def find_k_minima(k, p, arr): 
    classes, results = distance_from_each_in_list(p, arr)
    res = []
    for i in range(k):
        tmp = min(results)
        index = results.index(tmp)
        res.append(classes[index])
        classes.pop(index)
        results.pop(index)
    return res




x1 = [3, 4]
x2 = [0, 0, "D"]
x3 = [1, 5, "T"]
x4 = [3, -1, "O"]
x5 = [1, -1, "T"]
a1 = [x2, x3, x4, x5]

#a = find_k_minima(2, x1, a1)
#print(a)

#ACTUAL POINTS ON GRAPH:
#note T = triangle, S = square, C = circle

w1 = [1, 1, "T"]
w2 = [1, 3, "S"]
w3 = [1, 4, "S"]
w4 = [2, 2, "C"]
w5 = [2, 3, "S"]
w6 = [1.8, 3.8, "T"]
w7 =[2, 4, "C"]
w8 = [3, 2, "T"]
w9 = [3, 2.5, "T"]
w10 = [2.5, 5, "C"]
w11 = [4, 1, "S"]
w12 = [4, 2, "C"]
w13 = [5, 1, "T"]
w14 = [5, 3, "T"]

star = [2.2, 2.2]
diamond = [5, 5]
p = [5, 3]


pointsArr = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14]

m = find_k_minima(1, p, pointsArr)
print(m)