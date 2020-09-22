if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lar = lar2 = -999
    for x in arr:
        if x > lar:
           t = lar
           lar = x
           lar2 = t
        elif x > lar2 and x!=lar:
            lar2 = x 
    print(lar2)
