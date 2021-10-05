# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
enter = "y"
i = 0
total = 0
while enter == "y":
    add = int(input("Enter a number: "))
    i += 1
    total += add
    enter = input("Do you want to enter another number?: ")
print("Sum = " + str(total))
print("Average = " + str(total / i))
