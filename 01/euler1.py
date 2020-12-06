import numpy as np

def getMultiples(a,lim):
    return np.arange(lim)[::a][1:]

def getAllMultiples(aList,lim):
    return np.unique(np.concatenate([getMultiples(a,lim) for a in aList]))

mults = getAllMultiples([3,5],1000)
print(mults)
print(np.sum(mults))