def fibo_n(n):
    if n <=1:
        return n
    else:
        F = [0]*n
        F[0] = 1
        F[1] = 1
        for i in range(2,n):
            F[i] = F[i-1] + F[i-2]
        return F[-1]

if __name__ == '__main__':

    N = int(input())
    print (fibo_n(N))


