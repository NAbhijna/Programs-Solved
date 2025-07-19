def circle():
    r = int(input("Enter the radius (in cm): "))
    area = 3.14*r*r
    print(f"Area is: {area:2d} square cm")

def square(x):
    res = x*x
    print(f"Area is: {res} square cm")

def triangle():
    b = int(input("Enter the breadth (in cm): "))
    h = int(input("Enter the height (in cm): "))
    area = 0.5*b*h
    return area

def rectangle(l, b):
    area = l*b
    return area

while(True):
    print("-------------------------------------------------")
    print()
    print("1. Circle\n2. Square\n3. Triangle\n4. Rectangle\n")
    a = int(input("Enter your choice: "))
    match a:
        case 1:
            circle()

        case 2:
            s = int(input("Enter the length (in cm): "))
            square(s)
            
        case 3:
            res = triangle()
            print(f"Area is: {res} square cm")

        case 4:
            l = int(input("Enter the length (in cm): "))
            b = int(input("Enter the breadth (in cm):"))
            res = rectangle(l,b)
            print(f"Area is: {res} square cm")

        case 0:
            print("----->> Exiting Program <<-----")
            exit(0)

        case _:
            print("Invalid")
    