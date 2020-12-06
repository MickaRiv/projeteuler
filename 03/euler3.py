import numpy as np

def isDivisor(a,b):
    return np.mod(b,a) == 0

def isPrime(a):
    return not np.any([isDivisor(k,a) for k in range(2,int(a/2)+1)])
    
def primes(lim):
    return [i for i in range(2,lim+1) if isPrime(i)]

def primeFactors(num):
    print(num)
    if num == 1:
        return []
    i = 2
    while True:
        if isDivisor(i,num):
            return np.concatenate(([i],primeFactors(num//i)))
        i += 1

N = 600851475143
primeFact = primeFactors(N)
print(primeFact)
print(np.prod(primeFact))