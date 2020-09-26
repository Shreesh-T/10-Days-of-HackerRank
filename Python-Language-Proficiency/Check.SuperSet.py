# Enter your code here. Read input from STDIN. Print output to STDOUT
set1 = set(map(int, input().split()))
co = True
for i in range(int(input())):
    set2 = set(map(int, input().split()))
    if set2.issubset(set1) and len(set2)<len(set1) and co:
        a=2
    else: 
        co = False
print(co)
