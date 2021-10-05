# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
# <Get an int from the user and put it in studentNum. Make the message say "Enter the number of student grades: ">
studentNum = input("Enter the number of student grades: ")
# loop for the number of students
# <Make a for loop from 0 to studentNum>
for loop in range(1, int(studentNum)+1):
    # <Get an int from the user and put it in grade. Make the message say "Enter grade 1" or "Enter grade 2" ... (use
    # the i variable)> 
    i = int(input("Enter grade " + str(loop) + " :"))

    # <if grade is greater than or equal to 50, print out "Student has passed", else print "Student has failed">
    if i >= 50:
        print("Student has passed")
    else:
        print("Student has failed")
