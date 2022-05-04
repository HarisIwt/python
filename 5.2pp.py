"""
5.2pp task
Student ID 537318
Michael Liang
while loop
"""
print("I multiply your number together.")
userInput = int(input("Enter your next number,0 to finish: "))
sum = userInput
times = 0
while not userInput == 0:
    userInput = int(input("Enter your next number,0 to finish: "))
    # print(sum)
    times += 1
    if userInput == 0:
        break
    sum = userInput * sum
    # print(sum)
print("")
print("The product of your numbers is %d" % sum)
print("You entered %d numbers." % times)

