def inversion(a: int ,p: int):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = int(v/u)
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
        
    return x1%p

def main():
    p = 489573857
    a = 45682375
    print(inversion(a,p))


if __name__ == '__main__':
    main()