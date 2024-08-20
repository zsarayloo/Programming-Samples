def find_max(capacity, weights, values):
    value = 0.
    # write your code here
    U =[values[i]/weights[i] for i in range(len(weights))]

    
    p = list(zip(U,values,weights))
    p.sort(reverse=True)

    U,V,W = zip(*p)
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


if __name__ == '__main__':

    N,W = map(int,input().split())
    w = [0]* N
    c = [0]* N
    for i in range(N):
        c[i],w[i] = map(int,input().split())

    print(find_max(W,w,c))



