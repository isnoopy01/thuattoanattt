import math
def chuyenSoThanhMang(p: int , a: int, w: int ):
    matrixA = []
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    for i in range(t-1, -1, -1):
        tmp = pow(2,w*i)
        matrixA.append(math.floor(a/tmp))
        a = a % tmp
    return matrixA

def phepCong(matrixA: list(), matrixB: list(), w:int):
    l = len(matrixA)
    matrixC = list()
    matrixC.append((matrixA[l-1] + matrixB[l-1]) % pow(2,w))
    if(matrixA[l-1] + matrixB[l-1] > pow(2,w)):
        eps = 1
    else:
        eps = 0
        
    for i in range(l-2, -1, -1):
        matrixC.append((matrixA[i] + matrixB[i]+eps)%pow(2,w))
        if(matrixA[i] + matrixB[i]+eps > pow(2,w)):
            eps = 1
        else :
            eps = 0
    matrixC.reverse()
    return {'eps': eps , 'matrix': matrixC}

def phepTru(matrixA: list(), matrixB: list(), w:int):
    l = len(matrixA)
    matrixC= list()
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

    matrixC.reverse()
    return {'eps': eps , 'matrix': matrixC} 

def soSanh(matrixA: list(), matrixB: list()):
    for i in range(0, len(matrixA)):
        if(matrixA[i] > matrixB[i]):
            return True
    if(matrixA[len(matrixA)-1] == matrixB[len(matrixA)-1]):
        return True
    else:
        return False

def congTrenFp(matrixA: list(), matrixB: list(), w: int , p: int ):
    c = phepCong(matrixA, matrixB,w)
    f = chuyenSoThanhMang(p,p,w)
    while(c.get('eps') == 1):
            c = phepTru(c.get('matrix'), f, w)

    if(soSanh(c.get('matrix'),f) == True ) and (c.get('eps') == 0):
        c = phepTru(c.get('matrix'), f, w)
    
    return c

def main():
    p = 2147483647
    w = 8
    a = 2147483646
    b = 2147483643
    A = chuyenSoThanhMang(p,a,w)
    B = chuyenSoThanhMang(p,b,w)
    print(A)
    print(B)
    C = congTrenFp(A,B,w,p)
    print(C)
    

if __name__ == "__main__":
    main()