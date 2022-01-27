#INPUT:
# 2
# 3 12
# 1 6 9
# 5 9
# 3 4 4 4 8

#RESULT:
# 12
# 9

# https://www.hackerrank.com/challenges/unbounded-knapsack/problem

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    # Note: Since we have an infinite supply of a number to choose from, a 2-d array will not be necessary because we won't need to keep track of which elements is used. We can just use them. 
    # And since we are incrementing from the lowest weight up, we're guaranteed that the previous cases are prepared properly as we move forward, and we can override old solutions as we go.
    dp = [0] * (k + 1)
    for w in range(len(dp)):
        for idx in range(len(arr)):
            if arr[idx] <= w:
            	# The current best weight is either dp[w], which contains our previously computed example / base case, or taking one item from idx, or taking the value of one item at idx
            	# and getting the previously computed best sum at dp[w - arr[idx]]. Here, dp[w] represent the best weight we have found given the capacity w.
                dp[w] = max(dp[w], dp[w - arr[idx]] + arr[idx])
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    
    for i in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
