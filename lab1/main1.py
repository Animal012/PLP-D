import sys
import math
import time

coefficients = {1: 'a', 2: 'b', 3: 'c'}

def get_coefficient(index, line):
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

def calculation(a, b, c):
    roots = []
    D = float(b ** 2 - 4 * a * c)
    if D > 0.0:
        rt_1 = (-b + math.sqrt(D)) / (2 * a)
        rt_2 = (-b - math.sqrt(D)) / (2 * a)
        roots.extend([rt_1, rt_2])
    elif D == 0.0:
        rt_1 = (-b) / (2 * a)
        roots.append(rt_1)
    return roots

def linear(b, c):
    roots = [(-c) / b]
    return roots


def main():
    a, b, c = [get_coefficient(i, coefficients[i]) for i in range(1, 4)]
    if a != 0:
        roots = calculation(a, b, c)
    elif b != 0:
        roots = linear(b, c)
    elif c != 0:
        roots = []
    else:
        print("x - any number")
        time.sleep(10)
        return
    if b < 0 and c >= 0:
        print(f"Entered equation: {a}x^2{b}x+{c} = 0")
    elif c < 0 and b >= 0:
        print(f"Entered equation: {a}x^2+{b}x{c} = 0")
    elif b < 0 and c < 0:
        print(f"Entered equation: {a}x^2{b}x{c} = 0")
    else:
        print(f"Entered equation: {a}x^2+{b}x+{c} = 0")
    if len(roots) != 0:
        if len(roots) == 2:
            print("Two real roots")
            print(f"The first root: {roots[0]}")
            print(f"The second root: {roots[1]}")
        else:
            print(f"One real root: {roots[0]}")
    else:
        print("No roots")

    time.sleep(10)


if __name__ == "__main__":
    main()