#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    stack1 = a[::-1]
    stack2 = b[::-1]
    tracklist = []
    total = 0
    counting = 0
    while len(stack1) > 0:
        if total + stack1[-1] <= x:
            tmp = stack1.pop()
            tracklist.append(tmp)
            total += tmp
            counting += 1
        else:
            break
    
    totalB = 0
    while len(stack2) > 0:
        if totalB + stack2[-1] <= x:
            if total + stack2[-1] <= x:
                tmp = stack2.pop()
                total += tmp
                totalB += tmp
                counting += 1
            else:
                tmp = stack2.pop()
                total = total - tracklist.pop() + tmp
                totalB += tmp
        else:
            break
    return counting

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
