"""
Student ID 537318
Michael Liang
decision marking, this program can change newtons to kg

"""
ACCELERATION = 9.8 # acceleration constant

mass = 0;  # declare variable and assign initial values

weightStr = input("Enter an object's weight in Newtons")
weightFlo = float(weightStr)

mass = weightFlo / ACCELERATION

if mass > 500:
    print("It is too heavy.")

if mass < 100:
    print("It is too light.")
