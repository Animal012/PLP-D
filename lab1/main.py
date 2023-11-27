import sys
import math
import time

coefficients = {1: 'a', 2: 'b', 3: 'c'}

class SquareEquation:
    def __init__(self):
        self.kA = 0.0
        self.kB = 0.0
        self.kC = 0.0
        self.roots = []

    def get_coefficient(self, index, line):
        try:
            coefficient = int(sys.argv[index])
        except:
            print(f"Enter the coefficient {line.upper()}: ", end="")
            coefficient = ""
            while type(coefficient) != int:
                coefficient = input()
                try:
                    coefficient = int(coefficient)
                except:
                    print("Incorrect input, try again: ", end="")
        return coefficient

    def get_coefficients(self):
        self.kA, self.kB, self.kC = [self.get_coefficient(i, coefficients[i]) for i in range(1, 4)]

    def calculation(self):
        a = self.kA
        b = self.kB
        c = self.kC
        if a != 0.0:
            D = b ** 2 - 4 * a * c
            if D > 0.0:
                rt_1 = (-b + math.sqrt(D)) / (2 * a)
                rt_2 = (-b - math.sqrt(D)) / (2 * a)
                self.roots.extend([rt_1, rt_2])
            elif D == 0.0:
                rt_1 = (-b) / (2 * a)
                self.roots.append(rt_1)
        elif b != 0.0:
            self.roots.append(-c / b)

    def print_roots(self):
        if self.kB < 0 and self.kC >= 0:
            print(f"Entered equation: {self.kA}x^2{self.kB}x+{self.kC} = 0")
        elif self.kC < 0 and self.kB >= 0:
            print(f"Entered equation: {self.kA}x^2+{self.kB}x{self.kC} = 0")
        elif self.kB < 0 and self.kC < 0:
            print(f"Entered equation: {self.kA}x^2{self.kB}x{self.kC} = 0")
        else:
            print(f"Entered equation: {self.kA}x^2+{self.kB}x+{self.kC} = 0")
        if len(self.roots) != 0:
            if len(self.roots) == 2:
                print("Two real roots")
                print(f"The first root: {self.roots[0]}")
                print(f"The second root: {self.roots[1]}")
            else:
                print(f"One real root: {self.roots[0]}")
        elif self.kC != 0.0:
            print("No roots")
        else:
            print("x - any number")


def main():
    r = SquareEquation()
    r.get_coefficients()
    r.calculation()
    r.print_roots()
    time.sleep(10)


if __name__ == "__main__":
    main()