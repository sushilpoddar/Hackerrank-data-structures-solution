#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    vList = [0] * (n + 2)

    for q in queries:
        a, b, k = q[0], q[1], q[2]
        vList[a] += k
        vList[b + 1] -= k

    maximum = 0
    summation = 0
    # here i am using prefix sum algorithm for better performance
    for i in vList:
        summation += i
        maximum = max(maximum, summation)
    
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
