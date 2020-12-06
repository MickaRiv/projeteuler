import numpy as np
import sys

def isPalindromic(val):
    return str(val) == str(val)[::-1]

for i in range(1000,100,-1):
    for j in range(1000,i-100,-1):
        print(i,j)
        if isPalindromic(i*j):
            print(i,j,i*j)
            sys.exit()

