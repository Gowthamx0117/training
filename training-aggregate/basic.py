# print 2 if ip==1 and print 1 if ip == 2 (without using if else)
# a=int(input())
# print(3-a)
# print(2/a)

# print until the single digit comes(using loop)
# def fun(a):
#     b=0
#     while a>0:
#         d=a%10
#         b+=d
#         a//=10
#     return b

# a = int(input())
# while a >= 10:
#     a = fun(a)
# print(a)

# print until the single digit comes(using loop)
# a=int(input())
# print(a %9)

# a=input()
# b=a[::-1]
# print(a==b)

# a=input()
# s=[]
# for i in a:
#     b=int(i)
#     s.append(b)
# print(min(s))
# print(max(s))

# def fun(a):
#     min=1
#     max=0

#     while a>0:
#         d=a%10
#         if min>d:
#             min=d
#         if max<d:
#             max=d
#         a//=10
#     return min,max

# a=int(input())
# b,c=fun(a)
# print(b)
# print(c)

# a=int(input())
# temp=a
# b=0

# while a>0:
#     d=a%10
#     b+=d
#     a//=10

# c=temp%b
# if c==0:
#     print("harsad number")
# else:
#     print("not harsrad number")

# a=int(input())
# b=1
# temp=a
# z=a

# while a>0:
#     b*=10
#     a//=10
# b//=10
# while b > 0:
#     print(z // b)
#     z = z % b
#     b //= 10

# n = int(input())
# z1 = ''
# while n > 0:
#     d = n % 10
#     if d == 0:
#         z=9
#     else:
#         z=abs(9 - d)
#     s = str(z)
#     z1 += s
#     n //= 10
# print(int(z1))

# import math
# n=int(input())
# z=math.sqrt(n)
# print(int(z))

# import math
# n=int(input())
# z=int(math.sqrt(n))
# for i in range(1,n):
#     print(i*i,end=' ')

# def left(a):
#     z=len(a)
#     for i in range(1):
#         first = a[0]
#         for j in range(z-1):
#             a[j] = a[j + 1]
#         a[-1] = first
#     return a


# n=list(map(int,input().split()))
# print(*left(n))

def right(a):
    z = len(a)
    for i in range(1):
        last = a[-1]
        for j in range(z - 1, 0, -1):
            a[j] = a[j - 1]
        a[0] = last
    return a

n=list(map(int,input().split()))
print(*right(n))
