import math
def chuyenSoThanhMang(matrix: list() ,a: int , t: int, w: int ):
    for i in range(t-1, -1, -1):
        tmp = pow(2,w*i)
        matrix.append(math.floor(a/tmp))
        a = a % tmp



def main():
    p = 2147483649
    w = 8
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    matrix = []
    a = (int)(input("Nhap a: "))
    chuyenSoThanhMang(matrix,a,t,w)
    print(matrix)
    

if __name__ == "__main__":
    main()