#Classify a triangle based on side lengths

def triangle():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    if a + b >c and a + c >b and a + c >b:
        print("The triangle is possible")

    if a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    elif a != b or a != c or b != c:
        print("Scalene triangle")
    else:
        print("No triangle")

triangle()