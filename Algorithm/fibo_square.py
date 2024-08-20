def fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    n = n % 60  # Pisano period for modulo 10
    
    if n <= 1:
        return n
    
    previous, current = 0, 1
    
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    
    return current

def last_digit_sum_of_squares(n):
    if n <= 1:
        return n
    
    # F_n and F_(n+1) last digits
    Fn = fibonacci_last_digit(n)
    Fnp1 = fibonacci_last_digit(n + 1)
    
    # Last digit of the sum of squares
    return (Fn * Fnp1) % 10

if __name__ == '__main__':
    n = int(input())
    print(last_digit_sum_of_squares(n))

