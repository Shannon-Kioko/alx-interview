#!/usr/bin/python3
import numpy as np
import math
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
listy = np.arange(0, 9, 1.6)
listy.tolist()
# print([math.ceil(x) for x in listy])
# print([(x, x**2) for x in listy])/
np.random.seed(42)
rando = np.random.normal(6,1,(3,2))
randd= rando.tolist()
print(randd)
print([[row[i] for row in randd]for i in range(len(randd[0])) ])

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z', 'S', '45']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)