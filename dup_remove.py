n=int(input("Enter size of sorted array: "))
s=list(map(int,input("Enter sorted array elements: ").split()))
print(len(set(s)))
print(*set(s))