
def min_refills(distance, tank, stops):
    refill_num = 0
    stops = [0] + stops + [distance]  

    current_position = 0

    for i in range(1, len(stops)):
        if stops[i] - stops[i - 1] > tank:
            return -1

        if stops[i] - current_position > tank:
            current_position = stops[i - 1]
            refill_num += 1

    return refill_num

if __name__ == '__main__':

    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))

    print(min_refills(d, m, stops))
