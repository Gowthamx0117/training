# n=input()
# print(n[::-1])
def rev(x):
    if x == "":
        return ""
    else:
        return rev(x[1:]) + x[0]

a = input()
print(rev(a))
