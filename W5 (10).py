import math

# largest among three
def lar_3():
    a = float(input("Enter 1st Number : "))
    b = float(input("Enter 2nd Number : "))
    c = float(input("Enter 3rd Number : "))

    print(f"Max among {a,b,c} is {max(a,b,c)}")

# Area of rectangle
def ar_rect():
    l = float(input("Enter length of Rectangle : "))
    b = float(input("Enter breadth of Rectangle : "))

    print(f"Area of rectangle with dimenson {l , b} = {l*b}")


# Circumference of Cirlce
def circumference_circle():
    r = float(input("Enter radius of circle : "))
    pi = math.pi
    ar = 2 * pi * r
    print(f"circumference of circle of radius {r} = {ar}")
    
#Swap var
def swap_var():
    a = float(input("Enter 1st Number : "))
    b = float(input("Enter 2nd Number : "))
    
    print(f"Value before swapping a, b = {a,b}")

    a, b = b, a
    print(f"Value after swapping a, b = {a,b}")

# find dist
def distance():
    x1 = float(input("Enter Val of X1 : "))
    y1 = float(input("Enter Val of Y1 : "))
    x2 = float(input("Enter Val of X2 : "))
    y2 = float(input("Enter Val of Y2 : "))

    print(f"Distance Between {x1,y1} & {x2,y2} = { math.dist((x1, y1), (x2, y2))}")


#volume
def volume():
    print("Choose shape of your choice : ")
    print("1:Cylinder \n2:Cube\n3:Cuboid\n")
    shape = int(input("Enter your Choice : "))
    match shape:
        case 1:
            r = float(input("Enter radius of Base : "))
            h = float(input("Enter height of cylinder : "))
            vol_cyl = math.pi * r**2 * h
            print(f"Volume of cylinder = {vol_cyl}")
        case 2:
            s = float(input("Enter side of cube : "))
            vol_cube = s**3
            print(f"Volume of cube = {vol_cube}")
        case 3:
            l = float(input("Enter length of cuboid : "))
            b = float(input("Enter breadth of cuboid : "))
            h = float(input("Enter height of cuboid : "))
            vol_cuboid = l*b*h
            print(f"Volume of cuboid = {vol_cuboid}")
        case _:
            print("Invalid choice")


#Main
print("\tMenu\n1: Volume\n2: Distance\n3: Swap Var\n4: Circumference of Circle\n5: Largest among 3 numbers\n6: Area of Rectangle\n")            
ch = int(input("Enter your choice : "))

match ch:
        case 1: volume()

        case 2: distance()

        case 3: swap_var()

        case 4: circumference_circle()

        case 5: lar_3()

        case 6: ar_rect()

        case _: print("Invalid choice")
        
#volume()            
#distance()
#swap_var()    
#circumference_circle()
#lar_3()
#ar_rect()

