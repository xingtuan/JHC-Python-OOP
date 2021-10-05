# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
student = {}
student["Name"] = "James"
student["Age"] = 21
student["Course"] = "IT"
student["ID"] = "2016A001"
print(student)
print(student["Name"] + ":", student["ID"])
del student["Course"]
for i in student:
    print(student[i])