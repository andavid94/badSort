# Name: David An
# Course: CS325
# Desc: this program implements badSort and outputs the sorted array
#       to bad.out

import sys
import math
import numpy as np

# sort based on arr and alpha value
def badSort(arr, alpha):
    n = len(arr)
    if n == 2 and arr[0] > arr[1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp
    elif n > 2:
        m = int(math.ceil(alpha*n))
        if m == n and m > 2:
            m = n-1
        badSort(arr[:m], alpha)
        badSort(arr[n-m:n], alpha)
        badSort(arr[:m], alpha)

        


def main():

    # hijack stdout to print to .txt file
    orig_stdout = sys.stdout
    o = open('bad.out', 'w')
    sys.stdout = o

    with open('data.txt') as f:
        for line in f:
            
            # convert string into array of integers
            arr = np.array([int(i) for i in line.split()])
            
            alpha = float(2/3)
            badSort(arr, alpha)
            print(arr)

    sys.stdout = orig_stdout
    o.close()

if __name__ == "__main__":
    main()