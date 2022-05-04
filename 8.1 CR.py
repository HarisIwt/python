"""
8.1pp task
Student ID 537318
Haris Liang
More Complex Functions

"""


def getChecksum(barcode):
    sum = 0
    digit_count = 0

    for c in barcode:
        if c.isdigit():  # return a true
            digit_count += 1
            sum = int(c) + sum  # because c is a string, so we need change the type of c to int
    return sum, digit_count


again_or_not = 'y'
while (again_or_not == 'y'):
    barcode = input("Enter the barcode:")
    sum, count = getChecksum(barcode)
    print("The checksum is %d and %d digits were entered" % (sum, count))
    print("")
    again_or_not = input("Do you want to run this again? (y/n):")
    print("")
    if (again_or_not == 'n'):
        print("Goodbye!")
        break
