'''
-------------------------------------------------------------------------
Name:		problem1.py

Purpose: User is able to input temperature in Celsius and the program will convert the temperature to Fahrenheit

Author:	Chan. A

Created:	date in 12/07/2020
-------------------------------------------------------------------------
'''
# introduction to what program is
print("-Welcome to the Celsius to Fahrenheit Converter-")

# asks user for input
celsius = float(input("Please enter your temperature in Celsius (°C): "))

# convert Celsius to Fahrenheit using Celsius to Fahrenheit formula
convert = (celsius * 9/5) + 32

# print final statement of temperature in Fahrenheit
print("Temperature in Fahrenheit: " + str(convert) + "°F")