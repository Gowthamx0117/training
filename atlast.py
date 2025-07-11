n=list(map(int,input().split(",")))
n1=[]
n2=[]
for i in range(len(n)):
    s=n[i]
    if s==0:
        n2.append(s)
    else:
        n1.append(s)

n1.sort()
result = n1 + n2
print(result)