"""
4.2pp task
Student ID 537318
Michael Liang
calculate the tutorial cost

"""
CONSTVARA = 0.95
CONSTVARB = 1.5
CONSTVARC = 2.5
CONSTVARD = 3.5

ageStr = input("Hello, what is your age ? ")
ageInt = int(ageStr)
meal_costStr = input("How much your meal cost ?")
meal_costFlo = float(meal_costStr)

if ageInt <= 10:
    meal_surcharge = CONSTVARA

elif ageInt > 10 and ageInt <= 20:
    meal_surcharge = CONSTVARB

elif ageInt > 20 and ageInt <= 40:
    meal_surcharge = CONSTVARC

else:
    meal_surcharge = CONSTVARD

total_cost = meal_costFlo * meal_surcharge

print("your total cost is %.2f" % (total_cost))
