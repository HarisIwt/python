"""
11.3HD task
Student ID 537318
Haris Liang
Complex Class Definition and Usage

"""

# Add your comments here..

# import the class data from rocket.py
from rocket import *

# create a new rocket (feel free to the values!)
myRocket = Rocket("FalconX", "Tesla", 50)

# Print the rocket data - we need model, manufacturer and escape velocity.
print("The rocket is a %s series rocket manufactured by %s." % (myRocket.getModel(), myRocket.getManufacturer()))

# Make sure to ask myRocket for the values!
print("Escape velocity is set to: %d " % myRocket.getEscapeVelocity())
print("")

# Print the rocket status - is it landed?
# Hint - use getIsLanded and if statement
if myRocket.getIsLanded():
    print("The rocket is currently landed!")
else:
    print("The rocket is not landed!")
print("")

# Make the rocket take off
myRocket.takeOff()

# Print the rocket status now - is it flying?
# Hint - use getIsLanded and if statement
if myRocket.getIsLanded():
    print("The rocket is not flying!")
else:
    print("The rocket is currently flying!")

print("")

print("Rocket accelerating...")

# Make the rocket accelerate until it reaches escape velocity speed
# Hint - use a while loop
print("")
while myRocket.getSpeed() < myRocket.getEscapeVelocity():
    myRocket.accelerate()
    print("Rocket speed: %d" % myRocket.getSpeed())

print("")
print("Reached escape velocity!")
print("")

# Try to make the rocket land - you should get an error message as the speed is not zero!
myRocket.land()
print("")

print("Rocket decelerating...")
print("")
# Make the rocket decelerate until it reaches zero speed
# Hint - use a while loop
while myRocket.getSpeed() > 0:
    myRocket.decelerate()
    print("Rocket speed: %d" % myRocket.getSpeed())
print("")
# Try to make the rocket land - it should work now!
myRocket.land()

