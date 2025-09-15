import math

drink = input("Pick one (coke or pepsi) : ")
if drink == "coke":
    print("Here is your coke")
elif drink == "pepsi":
    print("Here is your pepsi")
else:
    print("Here is your water")

num1, operator, num2 = input("Enter Calculation: ").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator ==  "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Next time use + - * / %")

age = int(input("Enter Age: "))
if(age >=1) and (ag <=18):
    print("important birthday")