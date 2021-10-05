# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
correctPsw = 1111 # set password
# <Make an int called pswEntered and make it equal to 0>
pswEntered = 0
print("Program to Check Password")

# check password
# <Make a while loop to see if pswEntered is NOT equal to correctPsw>
while pswEntered != correctPsw:
    # <Get an int from the user and put it in pswEntered. Make the message say "Please enter password: ">
    pswEntered = int(input("Please enter password: "))
print("Password accepted!")

