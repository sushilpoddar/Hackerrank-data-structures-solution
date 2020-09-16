#!/bin/python3

import math
import os
import random
import re
import sys

def leftrotate(n, d, a):
    lis = [None for _ in range(n)]
    for i in range(len(a)):
        lis[i-d] = a[i]
    return lis

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = leftrotate(n, d, a)

    print(*result)
