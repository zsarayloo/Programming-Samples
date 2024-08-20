def fibo_n(n):
    # Pisano period length for m = 10 is 60
    n = n % 60
    
    if n <= 1:
        return n
    
    F_0, F_1 = 0, 1
    for _ in range(n - 1):
        F_0, F_1 = F_1, (F_0 + F_1) % 10

    return F_1

if __name__ == '__main__':
    N = int(input())
    print(fibo_n(N))



