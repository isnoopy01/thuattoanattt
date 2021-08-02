import math
import random

def gcd(a , b):
    while (b != 0):
        tmp = b
        b = a % b
        a = tmp
    return a

def toBin(n):
    temp = list()
    while (n>0):
        temp.append(n%2)
        n = math.floor(n/2)
 
    temp.reverse()
    return temp

def ModPower(a, k, n):
    b=1
    if (k == 1):
        return b
    else:
        k_Bin = toBin(k)
        k_Bin.reverse()
        if (k_Bin[0] == 1):
            b = a
        for i in range(1,len(k_Bin)):
            a = (a ** 2) % n
            if (k_Bin[i] == 1):
                b = (a * b) % n
 
        return(b)

def Decompose(n):
    j=0
    while (n % 2 == 1):
        n /= 2
        j += 1
 
    r = math.floor(n)
    return (j,r)

def Miller_Rabin(n,t):
    if (n == 2 or n == 3):
        return True
    s,r = Decompose(n)
    for i in (range(t)):
        a = random.randint(2,n-2)
        y = ModPower(a,r,n)
        if (y != 1 and y != (n - 1)):
            j = 1
            while (j <= (s-1) and y != (n-1)):
                y = (y ** 2) % n
                if (y == 1):
                    return False
                j += 1
            if (y != (n-1)):
                return False
 
    return True

def main():
    n = int(input())
    t = int(input())
    ktra = Miller_Rabin(n,t)
    if ktra == True:
        print(n, "-> La so nguyen to")
    else:
        print(n, "-> La hop so")

    

if __name__ == "__main__":
    main()