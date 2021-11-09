import random

def create(A,M,N):
    for i in range(N):
        for j in range(M):
            A[i][j] = random.randint(4, 51)

def print1(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print()

def swap(A,c1,c2,M):
    for j in range(M):
        A[c1][j], A[c2][j] = A[c2][j], A[c1][j]

def sortpro(A,a,N,M):
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap(A,j,j+1,M)

def sortreg(A,a,N,M):
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap(A,j,j+1,M)

def colx(A,j,a,N):
    for i in range(N):
        a.append(A[i][j])

def check1(A,M,a,N):
    colx(A, 0, a, N)
    sortpro(A, a, N, M)
    print1(A)
    print('1')
    print('--------------')


def check2(A,M,a,N):
    for i in range(M-1):
        for k in range(i+1,M):
            if A[i][0]==A[k][0]:
                colx(A, 1, a, N)
                sortreg(A,a,N,M)
                print1(A)
                print('2')
                print('--------------')
                return 0

def check3(A,M,a,N):
    for i in range(M):
        for k in range(M):
            if A[i][0]==A[k][1]:
                colx(A, 2, a, N)
                sortreg(A,a,N,M)
                print1(A)
                print('3')
                print('--------------')
                return 0

def checknum(a):
    p=1
    for n in a:
        if int(n) % 3 == 0:
            continue
        else:
            p += 1
    return p

def change(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] % 2 != 0 or checknum(str(A[i][j])) == True:
                continue
            else:
                A[i][j] = 0

def calc(A,s,k):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]%2!=0 or checknum(str(A[i][j]))==True:
                continue
            else:
                s += A[i][j]
                k += 1
    return s,k

def main():
    N = 8
    M = 5
    A = [[0] * M for i in range(N)]
    a = []
    create(A,M,N)
    print1(A)
    print('Original')
    print('--------------')
    print('Sum, K= '+str(calc(A, 0, 0)))
    print('--------------')
    check1(A,M,a,N)
    a.clear()
    check2(A,M,a,N)
    a.clear()
    check3(A,M,a,N)
    change(A)
    print1(A)
    print('Changed')
    print('--------------')


if __name__=='__main__':
    main()