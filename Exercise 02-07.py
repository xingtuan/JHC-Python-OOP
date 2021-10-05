# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/11
#  Get an animal as a string from the user and print it out:
print(input("Enter an animal: "))

# Get 2 numbers from the user and add them together:
print("Answer = " + str(int(input("Enter the first number: ")) + int(input("Enter the second number: "))))

# Get the length and width of a rectangle (as floats) and calculate and print the area and the perimeter of the rectangle:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area = " + str(length * width))
print("Perimeter = " + str(length * 2 + width * 2))

# Get the radius of a circle (as a float) and calculate and print the area of the circle.  Use 3.14 for π:
print("Area = " + str(3.14 * float(input("Enter the radius of the circle: ")) ** 2))