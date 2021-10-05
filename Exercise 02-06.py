# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/11
num1 = 2
num2 = 7

print("Arithmetic operations")
print("Number 1: " + str(num1) + " and Number 2: " + str(num2))
print()

answer = num1 + num2
print("Addition: " + str(num1) + " + " + str(num2) + " = " + str(answer))

# <Make answer equal to num1 - num2>
answer = num1 - num2
print("Subtraction: " + str(num1) + " - " + str(num2) + " = " + str(answer))

answer = num1 * num2
# <Make the output say  2 * 7 = 14" using the variables num1, num2 and answer>
print("Multiplication:" + str(num1) + " * " + str(num2) + " = " + str(answer))

# <Increase num1 by 5 using an Assignment Operator>
num1 += 5

# <Make answer equal to num2 / num1>
answer = num2 / num1
print("Division: " + str(num2) + " / " + str(num1) + " = " + str(answer))

# <Make answer equal to num2 modulus operator num1>
answer = num2 % num1
print("Remainder of " + str(num2) + " % " + str(num1) + " = " + str(answer))

print("Division when using double data types")
num3 = 2.0
num4 = 7.0

# <Make answer2 equal to num4 / num3>
answer2 = num4 / num3
print("Division: " + str(num4) + " div " + str(num3) + " = " + str(answer2))

# <Make answer2 equal to num4 modulus num3>
answer2 = num4 % num3
# <Make the output say "Remainder of 7.0 mod 2.0 = 1.0" using the variables num3, num4 and answer2>
print("Remainder of " + str(num4) + " mod " + str(num3) + " = " + str(answer2))
