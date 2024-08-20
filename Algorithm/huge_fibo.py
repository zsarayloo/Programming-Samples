def pisano_period(m):
    F_0, F_1 = 0, 1
    for i in range(0, m * m):
        F_0, F_1 = F_1, (F_0 + F_1) % m
        # A Pisano Period starts with 01
        if (F_0 == 0 and F_1 == 1):
            return i + 1

def fibo_n(n, m):
    # Getting the Pisano Period
    pisano_period_length = pisano_period(m)
    
    # Reduce n modulo the Pisano Period length
    n = n % pisano_period_length
    
    if n <= 1:
        return n
    
    F_0, F_1 = 0, 1
    for _ in range(n - 1):
        F_0, F_1 = F_1, (F_0 + F_1) % m
    
    return F_1

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(fibo_n(N, M))



