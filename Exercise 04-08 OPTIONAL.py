# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/15
user = input("Please enter word or sentence")
user = list(user)
output = []
band = 0
for i in range(0, len(user)):
    if user[i] in ("a", "e", "i", "o", "u"):
        output.append("X")
        band += 1
    else:
        output.append(user[i])
print("".join(output))
print("There are %d vowels in the word or sentence." % band)
