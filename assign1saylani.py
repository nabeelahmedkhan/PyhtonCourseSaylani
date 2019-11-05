""" Write a Python program to get the Python version you are using """

import platform
print(platform.python_version())

"""Write a Python program to display the current date and time."""

from datetime import datetime
now_date = datetime.now() 
print("Current datetime :", now_date)
dt_string = now_date.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

"""Write a python program which takes two inputs from user and print them
addition"""

inputint = []
inputint = input("input two numbers : ")
print("First two numbers addition: ",int(inputint[0]) + int(inputint[1]))

"""Write a Python program which accepts the user's first and last name and
print them in reverse order with a space between them"""

firstName = input("Enter first Name : ")
lastName = input("Enter Last Name : ")
print("".join(reversed(firstName)) +" "+ "".join(reversed(lastName)))
print(firstName[len(firstName)::-1] +" " + lastName[len(lastName)::-1])

"""Write a Python program which accepts the radius of a circle from the user
and compute the area."""

import math
radiusCircle = int(input("Enter Radius Of circle: "))
print("Area of circle is : ", 3.141*radiusCircle**2)
print("Area of circle is : ", math.pi*radiusCircle**2)

"""Write a Python program to print the following string in a specific format
(see the output).
Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are"""

stringPrint = ['Twinkle, twinkle, little star,',
               'How I wonder what you are!',
               'Up above the world so high,',
               'Like a diamond in the sky.']
n = 0
for j in range(0,6):
        if n == 0:    
            print(stringPrint[n])
        elif n == 1:
            print('\t',stringPrint[n])
        elif n == 2:
            print('\t\t',stringPrint[n])
        elif n == 3:
            print('\t\t',stringPrint[n])
        n+=1
        if n >= 4:
            n = 0
        