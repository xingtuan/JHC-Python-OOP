# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
for i in range(8):                # do this 8 times
    # print spaces first
    for j in range(0, 7-i):        # go from 0 to 7-i
        print(" ", end="")        # print space on same line

    # print stars
    for k in range(0, (2*i + 1)): # go from 0 to (2*i + 1)
        print("*", end="")        # print star on same line
    print()                       # print a new line

# now print the bottom half of the diamond
for i in range(7, 0, -1):
    for j in range(-1, 7-i):
        print(" ", end="")
    for k in range((2*i-1), 0, -1):
        print("*", end="")
    print()