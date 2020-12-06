import numpy as np

def isDivisor(a,b):
    return np.mod(b,a) == 0

def primeFactors(num):
    if num == 1:
        return [1]
    i = 2
    while True:
        if isDivisor(i,num):
            return np.concatenate(([i],primeFactors(num//i))).tolist()
        i += 1
        
def fuse(list1,list2):
    for val in list1:
        try:
            list2.remove(val)
        except:
            pass
    return list1+list2

facts = []
for i in range(1,21):
    primes = primeFactors(i)
    facts = fuse(facts,primes)
    
print(facts)
print(np.prod(facts))