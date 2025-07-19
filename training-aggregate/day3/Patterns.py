class pattern:
    def __init__(self):
        self.n= int(input())

    def square(self):
        for i in range(self.n):
            for j in range(self.n):
                print("*", end= " ")
            print()

    def increasing_triangle(self):
        for i in range(self.n):
            for j in range(i+1):
                print("*", end= " ")
            print()

    def decreasing_triangle(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print("*", end = " ")
            print()

    def right_triangle(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print(" ", end = " ")
            for k in range(i+1):
                print("*", end = " ")
            print()

    def left_triangle(self):
        for i in range(self.n):
            for j in range(i+1):
                print(" ", end = " ")
            for k in range(i,self.n):
                print("*", end = " ")
            print()

    def hill(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print(" ", end =" ")
            for k in range(i):
                print("*", end = " ")
            for l in range(i+1):
                print("*", end = " ")
            print()

    def reverse_hill(self):
        for i in range(self.n):
            for j in range(i+1):
                print(" ", end =" ")
            for k in range(i,self.n -1):
                print("*", end = " ")
            for l in range(i,self.n):
                print("*", end = " ")
            print()


    def diamond(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print(" ", end =" ")
            for k in range(i):
                print("*", end = " ")
            for l in range(i+1):
                print("*", end = " ")
            print()
        for i in range(self.n):
            for j in range(i+1):
                print(" ", end =" ")
            for k in range(i,self.n -1):
                print("*", end = " ")
            for l in range(i,self.n):
                print("*", end = " ")
            print()

class solution():
    def pattern_printing(self):
        a = pattern()
        print("SQUARE PATTERN")
        a.square()
        print("RIGHT TRIANGLE PATTERN")
        a.right_triangle()
        print("DECREASING TRIANGLE PATTERN")
        a.decreasing_triangle()
        print("LEFT TRIANGLE PATTERN")
        a.left_triangle()
        print("HILL PATTERN")
        a.hill()
        print("REVERSE HILL PATTERN")
        a.reverse_hill()
        print("DIAMOND PATTERN")
        a.diamond()


if __name__ == "__main__":
    S = solution()
    S.pattern_printing()
