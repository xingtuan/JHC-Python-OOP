# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
num = int(input("Enter the number for the times table: "))
for i in range(1, num+1):
    for ii in range(1, 6):
        print(i * ii, end="\t")
    print()