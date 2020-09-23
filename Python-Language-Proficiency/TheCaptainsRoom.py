# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
set1 = list(map(int, input().split()))
captain = (((sum(set(set1))*k) - (sum(set1)))//(k-1))
print(captain)
