"""
10.1CR task
Student ID 537318
Haris Liang
Code completion

"""

# question 1
i = 0
while i <= 4:
    print("Do you sell cheese cake", i, "here?")
    i = i + 1

# question 2
for i in range(0, 5):
    print("This is a cheese cake shop sir", i)

# question 3
cheeses = ["Original", "Lemon", "Strawberry", "Peanut"]
replies = ["Sorry", "No", "No", "Yes sir.. No"]

j = 0
for i in cheeses:
    print("Do you have any ", i, "?", sep='')
    print("%s" % replies[j])
    j = j + 1

    # question 4
cheeses = ["Original", "Lemon", "Strawberry", "Peanut"]
print("Welcome to the cheese cake shop.")
choice = input("Enter cheese: ").lower()
found = False
while found != True:
    for cheese in cheeses:
        if choice.find(cheese.lower()) != -1:
            found = True

    if found == False:
        print("No, we don't have that.")
        break
    else:
        print("Yes, we have that!")
