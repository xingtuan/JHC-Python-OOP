# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
# Introduction Messages
print("Welcome to programming in Python")
print("This program shows IF and logical operators")

print("Enter a number between 0 and 100: ")
num = int(input("Enter a number between 0 and 100: "))

# Test the numbers using relationship and logical operators
if num < 0 or num > 100:
    print("Number " + str(num) + " is not between 0 and 100")

if num >= 0 and num < 50:
    # <Make the code output "Number num is between 0 and 50" using the num variable>
    print("Number " + str(num) + " is between 0 and 50")

# <Make an ELSE IF statement to test if num is greater than or equal to 50 AND less than or equal to 100>
elif num >= 50 and num <= 100:
    print("Number " + str(num) + " is between 50 and 100")

# <Make an ELSE statement>
else:
    # <Make the code output "Number num is in the middle" using the num variable>
    print("Number " + str(num) + " is in the middle")