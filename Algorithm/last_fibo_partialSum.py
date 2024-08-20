def fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    # Pisano period for modulo 10 is 60
    n = n % 60
    
    if n <= 1:
        return n
    
    previous, current = 0, 1
    
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    
    return current

def fibonacci_partial_sum(m, n):
    if m > n:
        return 0
    
    # Last digit of S(n) - S(m-1)
    last_digit_sum_n = (fibonacci_last_digit(n + 2) - 1) % 10
    last_digit_sum_m_minus_1 = (fibonacci_last_digit(m + 1) - 1) % 10
    
    # Handling negative case since we're working with modulo
    return (last_digit_sum_n - last_digit_sum_m_minus_1 + 10) % 10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))

