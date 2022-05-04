"""
6.1pp task
Student ID 537318
Michael Liang
while and for loop
"""
again = "y"
while again == "y":
    letter = input("Enter the medicine codes (a,b,c,d,e and f): ")  # userinput
    print("Here are the result; ")

    setletter = set(letter)  # I use set function. return a set which disorder without repetition
    sortsetletter = sorted(setletter)  # then I use sorted function to sort it

    for i in sortsetletter:
        count = letter.count(i)  # use count function to calculate the sequence
        print("There were %d " % count + "%r" % i + " codes")  # output the result
    again = input("Do you want to run this program again (y/n) ? ")
    if again == "n":
        print("Goodbye")
        break
