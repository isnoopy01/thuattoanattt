def vetCan(T, P):
    loop = 0
    for i in range(len(T)):
        k = i
        for j in range(len(P)):
            if P[j] == T[k]:
                if j == len(P)-1:
                    return True, loop, i
                k += 1
            else:
                break
    return False

def main():
    # T = 'abacaabadcabacabaabb'
    # P = 'abacab'
    T = str(input())
    P = str(input())
    print(vetCan(T, P))


    

if __name__ == "__main__":
    main()