import math

def gcd(a,b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def prime(n):
    m = int(math.sqrt(n)+1)
    if n < 2:
        return 0
    else:
        for i in range(2,m):
            if(n%i == 0):
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
    if(prime(n)==1):
        return 'Khong phai Carmichael'
    for i in range(2,n):
        if(gcd(i,n)==1):
            if(power(i,n-1,n)!=1):
                return 'Khong phai Carmichael'
    return 'So Carmichael'

def main():
    n = int(input())
    print(n , '->', isCarmichaelNumber(n))

if __name__ == '__main__':
    main()