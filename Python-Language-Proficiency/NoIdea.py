# Enter your code here. Read input from STDIN. Print output to STDOUT
_, _ = input().split()
a = (input().split())
b = set(input().split())
c = set(input().split())
print(sum((x in b) - (x in c)for x in a))
