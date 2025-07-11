n=list(map(int,input().split()))
s=int(input())
e=[]

for i in range(len(n)):
    d=n[i]
    if d==s:
        e.append(d)
        break
    else:
        for j in range(i+1,len(n)):
            f=n[j]
            if d+f == s:
                g=[d,f]
                e.append(g)
                break

print(*e)