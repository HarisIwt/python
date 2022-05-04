"""
5.1pp task
Student ID 537318
Michael Liang
iteration using a for loop
"""
CONSTSTEP = 1000
stepminStr = input("Please enter your stair step rate in steps per minute: ")  # user enter steps per minute
stepminInt = int(stepminStr)
lengthOfTimeStr = input("Please enter the length of time in minute to display: ")  # user enter length of time in minute
lengthOfTimeInt = int(lengthOfTimeStr)

sum = 0
time = 1
print(" ")
print("Time Step total")
print("---------------")
for i in range(1, lengthOfTimeInt + 1):

    sum += stepminInt
    print("  %d    %d" % (i, sum))

    if sum < 1000:
        time += 1  # check the time when steps is over 1000.

if sum >= 1000:  #
    print("You reached the lookout at %d steps in %.01f minutes" % (CONSTSTEP, time))
else:
    print("You did not reach the lookout at %d steps!" % (CONSTSTEP))
