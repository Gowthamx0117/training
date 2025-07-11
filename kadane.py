def kadane(n):
    s=n[0]
    f=n[0]

    for i in range(1,len(n)):
        f=max(n[i],f+n[i])
        s=max(s,f)
    return s

n=list(map(int,input().split()))
print(kadane(n))
