# n = int(input())
# s = 0
# p = 1
# temp = n
# while temp > 0:
#     d = temp % 2
#     s += d * p
#     temp //= 2
#     p *= 10
# print(s)
# n1 = str(s)
# n2 = ''

# for i in n1:
#     if i == '1':
#         n2 += '0'
#     else:
#         n2 += '1'

# n2 = int(n2)
# print(n2)
# s1 = 0
# p1 = 1
# temp2 = n2
# while temp2 > 0:
#     d = temp2 % 10
#     s1 += d * p1
#     temp2 //= 10
#     p1 *= 2

# print(s1)

# n=input()
# n1=int(n)
# s=n1**2
# s1=str(s)
# if s1[-len(n):]==n:
#     print("Automorphic Number")
# else:
#     print("Not Automorphic Number")

# Find perfect number between the range 1 to 1000;

# n = int(input())
# m = int(input())
# perfect_numbers = []
# for num in range(n, m + 1):
#     factors_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             factors_sum += i
#     if factors_sum == num:
#         perfect_numbers.append(num)
# print(*perfect_numbers)


# m=int(input("Enter total no of vehicles: "))
# n=int(input("Enter no of wheels: "))

# s=(n//2)-m
# d=m-s
# print(s)
# print(d)


# n=list(map(int,input().split()))
# max=n[0]
# for i in n:
#     if i>max:
#         max=i

# n.remove(max)

# max1=n[0]
# for i in n:
#     if i>max1:
#         max1=i

# print(max1)

# n = input()
# words = n.split()

# longest_word = ''
# max_length = 0

# for word in words:
#     length = 0
#     for char in word:
#         length += 1

#     if length > max_length:
#         max_length = length
#         longest_word = word

# if max_length > 0:
#     print(max_length)
#     print(longest_word)
# else:
#     print(0)
#     print('')

