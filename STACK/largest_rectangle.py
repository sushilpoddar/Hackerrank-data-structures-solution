#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    res = 0
    height = h
    for i in range(len(height)):
        total = 0
        for j in range(i,len(height)):
            if height[j] >= height[i]:
                total += 1
            else:
                break
        for j in range(i-1, -1, -1):
            if height[j] >= height[i]:
                total += 1
            else:
                break
        res = max(res, total*height[i])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
