"""
7.1pp task
Student ID 537318
Haris Liang
Functions and Parameters

"""
PI = 3.1415
PAINTCOST = 6.99


def printPaintCost(hight, base, radius):
    again = 'y'
    while again == 'y':
        circle = radius * radius * PI
        triangele = (hight * base) / 2
        total = (circle + triangele) * PAINTCOST

        print("The area of the circle is %.02f meters squared" % circle)
        print("The area of the triangle is %.02f meters squared" % triangele)
        print("The total paint cost is $%.02f" % total)
        print("")
        again = input("Do you want to run this again? (y/n):")
        print("")
        if again == 'y':
            hight = int(input("Enter the triangle height :"))
            base = float(input("Enter the triangle base   :"))
            radius = float(input("Enter the circle radius   :"))
            print("")
        else:
            break

    print("Goodbye !")


hight = int(input("Enter the triangle height :"))
base = float(input("Enter the triangle base   :"))
radius = float(input("Enter the circle radius   :"))
print("")
printPaintCost(hight, base, radius)
