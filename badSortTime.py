# Name: David An
# Course: CS325
# Desc: this program implements badSort and outputs runtime for each array

import sys
import math
import numpy as np
import random
import time

def badSort(arr, alpha):
    n = arr.size

    if n == 2 and arr[0] > arr[1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp
    elif n > 2:
        m = int(math.ceil(alpha*n))
        
        # adjust m to account 
        if m == n and m > 2:
            m = n-1
        badSort(arr[:m], alpha)
        badSort(arr[n-m:n], alpha)
        badSort(arr[:m], alpha)
        


def main():

    # hijack stdout to print to .txt file
    orig_stdout = sys.stdout
    o = open('badSortTime23.out', 'w')
    sys.stdout = o

    arrSizes = [100, 150, 200, 300, 400]

    # iterate over every default array size
    for size in arrSizes:
        arr = []

        # populate arr with random integers
        for i in range(0, size):
            arr.append(random.randrange(10000))

        numpyArr = np.array(arr)

        alpha = float(2/3)
        start = time.process_time()
        badSort(numpyArr, alpha)
        elapsedTime = time.process_time() - start

        print(str(size) + ", " + str(elapsedTime))

    sys.stdout = orig_stdout
    o.close()

if __name__ == "__main__":
    main()