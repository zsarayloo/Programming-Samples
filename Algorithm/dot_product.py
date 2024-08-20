from itertools import permutations


def max_dot_product(P,C):

    P.sort(reverse = True)
    C.sort(reverse =True)
    sum = 0
    for i in range(len(P)):
        sum += P[i]*C[i]

    return sum


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
