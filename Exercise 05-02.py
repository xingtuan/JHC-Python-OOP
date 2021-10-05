# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
# <get an int from the user and put it in n. Make the message say "Enter the number of values to insert: "
n = int(input("Enter the number of values to insert: "))
# <make an empty list called myList>
myList = []
# <make a for loop from 0 to n>
for i in range(0, n):
    # <get an int from the user and put it in get_num. Make the message say "Enter a number to insert: ">
    get_num = int(input("Enter a number to insert: "))
    # <append get_num into the list>
    myList.append(get_num)

# <make a variable called sum and make it equal to sum(myList)
sum = sum(myList)
# <make a variable called average and make it equal to the average value
average = sum / n
# <print out the sum>
print("Sum is:", sum)
# <print out the average>
print("Average is:", average)
