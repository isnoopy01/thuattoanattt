import math
def chuyenSoThanhMang(matrixA: list() ,a: int , t: int, w: int ):
    for i in range(t-1, -1, -1):
        tmp = pow(2,w*i)
        matrixA.append(math.floor(a/tmp))
        a = a % tmp

def phepTru(matrixA: list(), matrixB: list(), matrixC: list(), w:int):
    l = len(matrixA)
    matrixC.append((matrixA[l-1] - matrixB[l-1]) % pow(2,w))
    if(matrixA[l-1] - matrixB[l-1] < 0):
        eps = 1
    else:
        eps = 0
    for i in range(l-2, -1, -1):
        matrixC.append((matrixA[i] - matrixB[i] - eps)%pow(2,w))
        if(matrixA[i] - matrixB[i] - eps < 0):
            eps = 1
        else :
            eps = 0
    return eps 

    
def main():
    p = 2147483649
    w = 8
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    matrixA = []
    matrixB = []
    matrixC = []
    a = (int)(input("Nhap a: "))
    b = (int)(input("Nhap b: "))
    chuyenSoThanhMang(matrixA,a,t,w)
    print(matrixA)
    chuyenSoThanhMang(matrixB,b,t,w)
    print(matrixB)
    e = phepTru(matrixA,matrixB,matrixC,w)
    print("e = %d" %e)
    matrixC.reverse()
    print(matrixC)
    

if __name__ == "__main__":
    main()