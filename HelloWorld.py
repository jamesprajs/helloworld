# importing calendar module
import calendar

print ("Hello you big beautiful World!")

# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = float(input("Enter celsius degrees: "))
# celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

# Program to display calendar of the given month and year

# yy = 2014  # year
# mm = 11    # month

# To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

# End of File
