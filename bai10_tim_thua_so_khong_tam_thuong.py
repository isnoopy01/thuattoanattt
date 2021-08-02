import math

def gcd(a,b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def PollardRho(n):
    a = 2
    b = 2
    for i in range(n):
        a = (a**2 + 1) % n
        b = (b**2 + 1) % n
        b = (b**2 + 1) % n
        d = gcd(a-b,n)
        if 1< d and d < n :
            return d
        elif d == n:
            return False

def main():
    n = int(input())
    print(PollardRho(n))

if __name__ == '__main__':
    main()
