import math


def triangle_area(base, height):
    s = str(base * height * 1 / 2)
    return s


def pythagorean_formula(lena, lenb):
    hypotenuse = str(math.sqrt(lena ** 2 + lenb ** 2))
    return hypotenuse


def heron_formula(a, b, c):
    p = (a + b + c) / 2
    s = (math.sqrt(p * (p - a) * (p - b) * (p - c)))
    return s


def inscribed_radius(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    radius = (s/p)
    return radius


def circumcise_radius(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    multiple = a*b*c
    fours = 4*s
    radius = multiple/fours
    return radius


def find_median(a, b, c):
    bb = b**2
    aa = a**2
    cc = c**2
    median = math.sqrt(2*bb + 2*cc - aa)/2
    return median


def find_bisector(a, b, c):
    p = (a + b + c) / 2
    first = 2 / (b + c)
    second = math.sqrt(b*c*p*(p - a))
    bisector = first * second
    return bisector


while True:
    try:
        print("""
                    ████████╗██████╗░██╗░█████╗░███╗░░██╗░██████╗░██╗░░░░░███████╗
                    ╚══██╔══╝██╔══██╗██║██╔══██╗████╗░██║██╔════╝░██║░░░░░██╔════╝
                    ░░░██║░░░██████╔╝██║███████║██╔██╗██║██║░░██╗░██║░░░░░█████╗░░
                    ░░░██║░░░██╔══██╗██║██╔══██║██║╚████║██║░░╚██╗██║░░░░░██╔══╝░░
                    ░░░██║░░░██║░░██║██║██║░░██║██║░╚███║╚██████╔╝███████╗███████╗
                    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝""")
        print("""
                    [ 1 ] Triangle Area
                    [ 2 ] Pythagorean Formula
                    [ 3 ] Heron Formula
                    [ 4 ] The Radius of  The Inscribed Circle of a Triangle
                    [ 5 ] The Radius of  The Circumscribed circle of a Triangle
                    [ 6 ] The Median of a Triangle
                    [ 7 ] The Bisector of a Triangle
                    [ Q ] For quit""")
        option = input("Enter Option: ")
        if option.isdigit():
            if int(option) == 1:
                Base = input("base: ")
                length = input("length: ")
                if float(Base) <= 0 or float(length) <= 0:
                    print("INVALID INPUT.")
                    input()
                    continue
                else:
                    print("Triangle area is", triangle_area(float(Base), float(length)))
                    input()
            elif int(option) == 2:
                side1 = input("length(a): ")
                side2 = input("length(b): ")
                if float(side1) <= 0 or float(side2) <= 0:
                    print("INVALID INPUT")
                    input()
                    continue
                else:
                    print("length(c):", pythagorean_formula(float(side1), float(side2)))
                    input()
            elif int(option) == 3:
                side1 = input("len(a): ")
                side2 = input("len(b): ")
                side3 = input("len(c): ")
                if float(side1) <= 0 or float(side2) <= 0 or float(side3) <= 0:
                    print("INVALID INPUT")
                    input()
                    continue
                else:
                    S = heron_formula(float(side1), float(side2), float(side3))
                    if S <= 0:
                        print("""The sum of the length of any two sides of a triangle
should be greater than the length of the third side.""")
                        input()
                    else:
                        print("Triangle area is", S)
                        input()
            elif int(option) == 4:
                side1 = input("len(a): ")
                side2 = input("len(b): ")
                side3 = input("len(c): ")
                if float(side1) <= 0 or float(side2) <= 0 or float(side3) <= 0:
                    print("INVALID INPUT")
                    input()
                    continue
                else:
                    r = inscribed_radius(float(side1), float(side2), float(side3))
                    if r <= 0:
                        print("""The sum of the length of any two sides of a triangle
should be greater than the length of the third side.""")
                        input()
                    else:
                        print("the radius(r) of the inscribed circle is", r)
                        input()
            elif int(option) == 5:
                side1 = input("len(a): ")
                side2 = input("len(b): ")
                side3 = input("len(c): ")
                if float(side1) <= 0 or float(side2) <= 0 or float(side3) <= 0:
                    print("INVALID INPUT")
                    input()
                    continue
                elif side1 + side2 <= side3 or side3 + side2 <= side1 or side1 + side3 <= side2:
                    print("""The sum of the length of any two sides of a triangle
should be greater than the length of the third side.""")
                    input()
                else:
                    R = circumcise_radius(float(side1), float(side2), float(side3))
                    print("the radius(R) of the  circle is", R)
                    input()
            elif int(option) == 6:
                side1 = input("the opposing side: ")
                side2 = input("len(b): ")
                side3 = input("len(c): ")
                if float(side1) <= 0 or float(side2) <= 0 or float(side3) <= 0:
                    print("INVALID INPUT")
                    input()
                    continue
                else:
                    print(find_median(float(side1), float(side2), float(side3)))
                    input()
            elif int(option) == 7:
                side1 = input("the opposing side: ")
                side2 = input("len(b): ")
                side3 = input("len(c): ")
                if float(side1) <= 0 or float(side2) <= 0 or float(side3) <= 0:
                    print("INVALID INPUT")
                    input()
                    continue
                else:
                    print(find_bisector(float(side1), float(side2), float(side3)))
                    input()
            else:
                continue
        elif option == "q" or option == "Q":
            quit()
        else:
            continue
    except ValueError:
        print("INVALID INPUT")
        input()
        continue
    except ZeroDivisionError:
        print("INVALID INPUT")
        input()
