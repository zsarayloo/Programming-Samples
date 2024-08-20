

def GCD(a,b):
    if a<=b:
        c = a
        a = b
        b = c
    
    while True:

        R = a%b
        if R == 0:
             return b

            
        a = b 
        b = R





if __name__ == '__main__':
    a,b = map(int,input().split())
    lcm = int( (a*b)/GCD(a,b))
    print (lcm)

        





















