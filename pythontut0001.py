import sys

my_age = 18
legal_age = 21
people_name = "John"

#single comment

'''
multiple comments
'''

str_1="\"This is a quote\""
print(str_1)
'''
New Line: \n
Backslash: \\
Single quote: \'
backspace: \b
tab:: \t
'''

print("hello", people_name)
print(sys.maxsize)
print(sys.float_info.max)
print("Cast", type(int(5.4)))
print("Cast", type(str(5.4)))
print("Cast", type(chr(97)))
print("Cast", type(ord('a')))
print("Cast", type(float(2)))

num1 = "1"
num2 = "2"

print("1 + 2 = ", (int(num1) + int(num2)))

name = input("What is your name? ")
print("Hello, " + name)

num_1, num_2 = input("Enter 2 numbers: ").split()
num_1 = int(num_1)
num_2 = int(num_2)
sum_1 = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2
remainder = num_1 % num_2

print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, difference))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))

miles = int(input("Enter miles: "))
kilometers = miles * 1.60934
print("{} miles = {} kilometers".format(miles, kilometers))
