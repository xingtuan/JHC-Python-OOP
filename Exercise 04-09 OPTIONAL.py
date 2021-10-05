# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
user = input("Please enter a word or sentence: ")
user = list(user)
for i in range(0, len(user)):
    if user[i] == "x":
        print("This has the letter ‘x’ in it")
        break
else:
    print("This does not have the letter ‘x’ in it")
