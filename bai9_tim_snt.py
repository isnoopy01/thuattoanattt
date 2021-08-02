import math
def sang(n):
    arr = []
    ktra = [True]*(n+1)
    p = 2
    while (p * p <= n):
        if (ktra[p] == True):
            for i in range(p * p, n + 1, p):
                ktra[i] = False
        p += 1
 
    for i in range(2, n):
        if ktra[i]:
            arr.append(i)
            
    return arr
def main():
    n = int(input())
    print(sang(n))



if __name__ == '__main__':
    main()
