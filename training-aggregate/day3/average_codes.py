# Right Triangle

# def pattern(n):
#     for i in range(n):
#         print(" ",end=' ')
#         for j in range(0,i+1):
#             print("*",end=' ')
#         print()

# n=int(input())
# pattern(n)

# Right Triangle(reverse)

# def pattern(n):
#     for i in range(n):
#         print(" ",end=' ')
#         for j in range(i+1,n+1):
#             print("*",end=' ')
#         print()

# n=int(input())
# pattern(n)

# Right Triangle left side

# def pattern(n):
#     for i in range(n):
#         for j in range(n-1-i):
#             print(" ",end=' ')
#         for k in range(0,i+1):
#             print("*",end=' ')
#         print()

# n=int(input())
# pattern(n)

# Right triangle left side (reverse)

# def pattern(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end=' ')
#         for k in range(n-i):
#             print("*",end=' ')
#         print()

# n=int(input())
# pattern(n)

# Right tirangle right and left mirrored

# def pattern(n):
#     for i in range(1, n + 1):
#         # Left triangle
#         for j in range(i):
#             print("*", end=" ")

#         # Middle space (each row has 2*(n - i) spaces)
#         for space in range(2 * (n - i)):
#             print(" ", end=" ")  # two spaces for each to match star width

#         # Right triangle
#         for j in range(i):
#             print("*", end=" ")

#         print()  # new line

# n = int(input("Enter number of rows: "))
# pattern(n)

# Hollow pattern

# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j ==0:
#                 print("*",end=" ")
#             elif i==n-1 or j==n-1:
#                 print("*",end=' ')
#             else:
#                 print(" ",end=' ')
#         print()

# n=int(input())
# pattern(n)

# 1 0 altrenate print pattern

# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if (i+j)%2==0:
#                 print("1",end=' ')
#             else:
#                 print("0",end=' ')
#         print()

# n=int(input())
# pattern(n)

# pyramid pattern

# def pattern(n):
#     for i in range(n):
#         for j in range(i,n):
#             print(" ",end=' ')
#         for k in range(i):
#             print("*",end=' ')
#         for l in range(i+1):
#             print("*",end=' ')
#         print()


# n=int(input())
# pattern(n)

# Reverse pyramid pattern

# def pattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(" ",end=' ')
#         for k in range(i,n-1):
#             print("*",end=' ')
#         for l in range(i,n):
#             print("*",end=' ')
#         print()


# n=int(input())
# pattern(n)

# Parallelogram pattern

# def pattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(" ",end=' ')
#         for k in range(i):
#             print("*",end=' ')
#         for l in range(i,n):
#             print("*",end=' ')
#         print()


# n=int(input())
# pattern(n)

# Diagonal pattern

# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if i==j or j==n-i-1:
#                 print("*",end=' ')
#             else:
#                 print(" ",end=" ")
#         print()


# n=int(input())
# pattern(n)

# Leet code 66 

# n=list(map(int,input().split()))
# a=''
# for i in n:
#     a+=str(i)

# a1=str(int(a)+1)
# s=[]
# for i in a1:
#     s.append(int(i))
# print(s)

print("end")