# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
# <make an empty list called fib>

fib = []
# <append 0 to the fib list>
fib.append(0)
# <append 1 to the fib list>
fib.append(1)

# <make a for loop from 2 to 10>
for i in range(2, 10):
    # <append to the fib list the previous element plus the element before the previous element>
    fib.append(fib[i - 1] + fib[i - 2])
# <make a for loop to print out the elements in the fib list>
for i in fib:
    print(i, end=", ")
