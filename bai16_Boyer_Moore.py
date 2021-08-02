import math
import random

def lastOccurrence(T,P):
    A = set(T)
    L = {}
    for i in A:
        try:
            L[i] = P.rindex(i)
        except:
            L[i] = -1
    return L

def boyer_moore(T, P):
    L = lastOccurrence(T,P)
    j = len(P)-1
    i = j
    m = len(P)
    dem = 0
    while i < len(T):
        dem += 1
        if T[i] == P[j]:
            if j == 0:
                return True, dem, i
            i = i-1
            j = j-1
        else:
            i = i+m-min(j, 1+L[T[i]])
            j = m-1
    return False

def main():
    # T = 'abacaabadcabacabaabb'
    # P = 'abacab'
    T = str(input())
    P = str(input())
    
    print(boyer_moore(T, P))


    

if __name__ == "__main__":
    main()