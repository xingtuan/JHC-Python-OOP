# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
i = 3   # counter for number of logins
# <Make a variable called done and make it equal to false>
done = False
print("Program to Change Password");
print("Your password has expired and you have " + str(i) + " chances left to change your password")

# While password is not entered correctly AND more than 0 chances
# <Make a while loop to say while not done and i is greater than 0>
while not done and i > 0:
    newPsw = input("Please enter your new password: ")

    # <Get input from the user and put it in pswEntered>
    pswEntered = input("Please enter your new password again: ")
    # change password correct
    # <Make an IF statement to see if newPsw equals pswEntered>
    if newPsw == pswEntered:
        # <Make done equal to true>
        done = True
    else:
        print("Error in entering password, please try again")
        # <Make i decrease by 1>
        i -= 1
        # <Print out you have i chances left>
        print("You have " + str(i) + " changes left.")


# <Make an IF statement to see if i is less than or equal to 0>
if i <= 0:
    print("Password not changed") # password accepted
else:
    print("Password accepted!")
