a = input()
n = len(a)
s = []

for i in range(n):
    r = a[i:] + a[:i]
    s.append(int(r))

print(max(s)-min(s))
