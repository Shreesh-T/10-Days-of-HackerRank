# Enter your code here. Read input from STDIN. Print output to STDOUT
lower,upper,odd,even=[],[],[],[]
for a in sorted(input()):
    if a.isalpha():
        if a.isupper():
            upper.append(a)
        else:
            lower.append(a)
    else:
        if int(a)%2 == 0:
            even.append(a)
        else:
            odd.append(a)
print("".join(lower+upper+odd+even))
