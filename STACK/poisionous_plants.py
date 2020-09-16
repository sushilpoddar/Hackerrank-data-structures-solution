#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(arr): # arr-->[6 5 8 4 7 10 9]
    # create a stack which contain the 0th index element
    stack = [0]
    # create a list of days which showing the plant die on that days
    days = [0] * len(arr)
    # create a variable to store minimum value and update time to time
    minimum = arr[0]
    # create a variable to store the result which is max of days list
    result = 0
    # iterate over array from 1 to len(Array)
    for index in range(1, len(arr)):  
        # if current index element is > than previous index element then update days list
        if arr[index] > arr[index - 1]:
            # mark that index in days list as 1
            days[index] = 1
        # update the minimum value
        minimum = min(minimum, arr[index])
        # iterate while stack is not empty as well as stack last index in array is >= current index element
        while stack and arr[stack[-1]] >= arr[index]:
            # check condition wheather current index element is > than minimum or not.
            if arr[index] > minimum:
                # if condition is true than update days list 
                days[index] = max(days[index], days[stack[-1]] + 1)
            # wheather if condition is true or not ..that element pop from the stack  
            stack.pop()
        # update the result which is max of current result or days index value
        result = max(result, days[index])
        # current index is append to the stack 
        stack.append(index)
    # return result
    return result  

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = poisonousPlants(p)
    print(result)
