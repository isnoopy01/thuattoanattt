def timTienTo(n, P):
    tt = []
    s = ''
    for i in range(n):
        s = s + P[i]
        tt.append(s)
    return list(reversed(tt))


def timHauTo(n, P):
    ht = []
    s = ''
    for i in range(n-1, 0, -1):
        s = P[i]+s
        ht.append(s)
    return list(reversed(ht))


def failure(P):
    F = [0]*len(P)
    F[0] = -1
    for j in range(2, len(F)):

        tt = timTienTo(j, P)
        ht = timHauTo(j, P)

        for i in tt:
            try:
                ht.index(i)
                F[j] = len(i)
                if F[j] != 0:
                    break
            except:
                continue

    return F


def knuthMorisPratt(T, P):
    F = failure(P)
    i = 0
    j = 0
    loop = 0
    while i < len(T):
        loop += 1
        if T[i] == P[j]:
            i += 1
            j += 1
        if j == len(P):
            return True, i-j, loop
        elif i < len(T) and P[j] != T[i]:
            if j != 0:
                j = F[j-1]
            else:
                i += 1
    return False

def main():
    #T = 'abaaabadcabacabaabb'
    #P = 'abacab'
    T = str(input())
    P = str(input())
    print(knuthMorisPratt(T, P))


if __name__ == "__main__":
    main()