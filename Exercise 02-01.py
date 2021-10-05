# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/11
meal = 44.50
tax = 0.0675
tip = 0.15
meal += meal * tax
total = meal + meal * tip
print("Total cost of meal: $%.2f" % total)