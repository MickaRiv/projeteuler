import numpy as np

def Fibonacci(lim):
    fibList = [1,2]
    while fibList[-2]+fibList[-1] <= lim:
        fibList.append(fibList[-2]+fibList[-1])
    return fibList

fib = Fibonacci(4e6)
print(fib)
print(fib[1::3])
print(np.sum(fib[1::3]))