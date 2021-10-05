# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
print("Program to show high and low numbers")

# Get input and calculate number
# <Get an int from the user and put it into num1. Make it say "Enter a number">
num1 = int(input("Enter a number: "))
if num1 > 50:
    print(str(num1) + " is a high number")

# <Make an if statement to see if num1 is less than 50>
if num1 < 50:
    print(str(num1) + " is a low number")

# <Make an if statement to see if num1 is equal to 50>
if num1 == 50:
    # <Print out "50 is in the middle" using the num1 variable>
    print("50 is in the middle")
