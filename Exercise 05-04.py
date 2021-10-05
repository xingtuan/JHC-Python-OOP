# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
marks = {"Sam": 90.5, "Jane": 85.4, "Max": 92.3, "Alice": 64.5, "John": 69.4}
sum = 0
for i in marks:
    sum += marks[i]
print("Sum:", sum)
print("Average:", sum / len(marks))