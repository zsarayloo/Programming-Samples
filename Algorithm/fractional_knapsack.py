from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    p = list(zip(values,weights))
    p.sort(reverse=True)

    V,W = zip(*p)
    V = list(V)
    W = list(W)
    
    w_total = 0
    R = capacity

    for i in range(len(V)):
        if W[i] <= R and w_total <capacity:
            if W[i]+w_total <=capacity :
                value += V[i]
                w_total += W[i]
                R -= W[i]
                if R <=0 :
                    return value

            else:
                value += V[i]*(R/W[i])
                
                w_total += R
                R = 0
                return value
        else:
            value += V[i]* (R/W[i])
            w_total +=R
            return value
    return value





    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
