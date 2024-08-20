def change_coin(n):
    R = n%10
    if R == 0:
        C1 = int(n/10)
        C2 = 0
        C3 = 0
        return (C1,C2,C3)
    else:
        C1 = int(n/10)
        R2 = R%5
        if R2 == 0:
            C2 = int (R/5)
            C3 = 0
            return (C1,C2,C3)
        else:
            C2 = int (R/5)
            C3 = R2
            return (C1,C2,C3)

if __name__ == '__main__':
    n = int(input())
    #print(change_coin(n))
    #print('other Sol:')
    print (int(n/10)+int((n%10)/5)+n%5)


    
