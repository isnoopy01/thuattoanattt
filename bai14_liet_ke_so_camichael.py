import math

def gcd(a,b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def prime(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return 0
    return 1

def power(x,y,mod):
    if (y == 0):
        return 1

    temp = power(x, int(y/2), mod) % mod
    temp = (temp * temp) % mod

    if (y % 2 == 1):
        temp = (temp * x) % mod
    return temp

def isCarmichaelNumber(n):
    for i in range(2,n):
        if(gcd(i,n)==1):
            if(power(i,n-1,n)!=1 or prime(n)==1):
                return 0
    return 1

def carmichaelNumber(n):
    arr = list()
    for i in range(561,n+1):
        if(isCarmichaelNumber(i)==1):
            arr.append(i)
    return arr


def main():
    n = int(input())
    print(carmichaelNumber(n))

if __name__ == '__main__':
    main()