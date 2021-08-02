import math

def phanTich(n):
    snt = []
    somu = []
    for i in range(2,n+1):
        dem = 0
        while n%i==0:
            dem +=1
            n /=i
        if dem > 0:
            snt.append(i)
            somu.append(dem)
    
    return {'snt': snt , 'somu': somu}
def main():
    n = int(input())
    coso = phanTich(n).get('snt')
    somu = phanTich(n).get('somu')
    print("coso =",coso)
    print("somu =",somu)

if __name__ == '__main__':
    main()