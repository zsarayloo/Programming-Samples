


def find_maximum_pairwise(N):

    N.sort(reverse = True)
    return (N[0]*N[1])

if __name__ == '__main__':
    num = input()
    Input = input().split()
    Input = [int(number) for number in Input]
    print (find_maximum_pairwise(Input))








