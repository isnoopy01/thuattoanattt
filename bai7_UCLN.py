def gcd(a: int , b: int):
    while (b != 0):
        tmp = b
        b = a % b
        a = tmp

    return a

def main():
    a = (int)(input("Nhap a: "))
    b = (int)(input("Nhap b: "))
    print("GCD = " ,gcd(a,b))


if __name__ == "__main__":
    main()