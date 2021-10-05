# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
# <Make answer equal 44>
answer = 44
# <Make count equal 5>
count = 5

# <Make a while loop for while count is greater than 0>
while count > 0:
    # <Get an int from the user and put it in guess. Make the message say "Enter a number: ">
    guess = int(input("Enter a number: "))
    # <Make an if statement to see if guess equals answer>
    if guess == answer:
        # <Print "You are correct">
        print("You are correct")
        break
    # <Decrease count by 1>
    count -= 1
    print("Wrong. Try again. You have " + str(count) + " more tries.")

