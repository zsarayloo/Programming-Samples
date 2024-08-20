def fibonacci_sum(n):
    if n <= 1:
        return n
    
    # Pisano period length for m = 10 is 60
    n = (n + 2) % 60
    
    if n <= 1:
        return (n - 1) % 10

    previous, current = 0, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    
    # The sum of the first n Fibonacci numbers is F(n+2) - 1
    return (current - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))

