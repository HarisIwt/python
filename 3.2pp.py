"""
Student ID 537318
Michael Liang
Description: This program purpose is ask from the user and display the output.

"""

temperature = float(input("Please enter a temperature in fahrenheit."))  # user input a temperature

celsius = (9 / 5) * temperature + 32  # The program converted to Celsius according this temperature

kelvin = temperature + 273.15  # The program converted to kelvin, through calculate.

print("Temperature is %.1f" % (temperature))  # Display the resulting information properly.
print("Celsius is %.1f" % (celsius))
print("Kelvin is %.2f" % (kelvin))
