# PRINTING
# print "This is python 2 syntax"
print("Python 3 syntax")

# STRINGS
# can be defined with "" or ''
# can combine multiple strings using +

print("You can use double quotes")
print('or single quotes!')
print("Concatenate strings " + "with " + "+")

# HANDLING ERRORS
# print("How do you make a hot dog stand?') -> SyntaxError: EOL while scanning string literal
# print(You take away its chair!) -> SyntaxError: invalid syntax

# VARIABLES
greeting_message = "Welcome to Codecademy!"
current_excercise = 5

# ARITHMETIC

# combinations of arithmetical operators follow the usual order of operations
# modulo operator %: returns the remainder after division
mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12
is_this_number_odd = 15 % 2 # 1
is_this_number_divisible_by_seven = 133 % 7 # 0 

# UPDATING VARIABLES
# shorthand: +=
money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price

sandwich_price += sales_tax
money_in_wallet -= sandwich_price

# NUMBERS
# types: integer, float (a number with a decimal point)
# can define float by including a decimal point or by using scientific notation (e indicates the power of 10)
float1 = 1.5e2 # 150.0

cucumbers = 2
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost) # 6.5

# in Python 2, diving 2 integers produces an integer
# this results in problem if numbers don't divide evenly (EX: 7/2 -> 3)
# overcome this by adding decimal point to numerator and/or denominator
quotient1 = 7./2  # the value of quotient1 is 3.5
quotient2 = 7/2.  # the value of quotient2 is 3.5
quotient3 = 7./2. # the value of quotient3 is 3.5

cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers/num_people
print(whole_cucumbers_per_person) # 16

float_cucumbers_per_person = float(cucumbers)/6
print(float_cucumbers_per_person) # 16.6666666667

# MULTILINE STRINGS
# use triple quotes
address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""
# if it's not assigned to a variable, it functions as a multiline comment
"""The following piece of code does the following steps:
takes in some input
does An Important Calculation
returns the modified input and a string that says "Success!" or "Failure..."
"""

# BOOLEANS
# datatype with only two possible values: True and False
# True corresponds to integer value of 1, False corresponds to integer value of 0

"""Hi! I'm Maria and I live in script.py.
I'm an expert Python coder.
I'm 21 years old and I plan to program cool stuff forever.
"""

age_is_12 = False
name_is_maria = True

# VALUEERROR
# Python automatically assigns a variable the appropriate datatype based on the value it is given
# we can convert between datatypes (EX: str() to convert integer to string)
age = 26
print("I am " + str(age) + " years old!") # "I am 26 years old!"

number1 = "100"
number2 = "10"

string_addition = number1 + number2 # "10010"
int_addition = int(number1) + int(number2) # 110
# using int() on a float will round the number down
string_num = "7.5"
print(int(string_num)) # 7
print(float(string_num)) # 7.5

## STRINGS & CONSOLE OUTPUT ##

# STRINGS
# string can contain letters, numbers, and symbols
# strings need to be within quotes
name = "Ryan"
age = "19"
food = "cheese"

# ESCAPING CHARACTERS
# 'There's a snake in my boot!' - Python thinks second apostrophe marks end of string
# need backslash 
fixed_string = 'There\'s a snake in my boot!'

# ACCESS BY INDEX
# Each character in a string is assigned a number. This number is called the index. 
# Python indices start at 0
fifth_letter = "MONTY"[4]
print(fifth_letter) # "Y"

# STRING METHODS
# len(), lower(), upper(), str()
parrot = "Norwegian Blue"
print(len(parrot)) # 14
print(parrot.lower()) # "norwegian blue"
print(parrot.upper()) # "NORWEGIAN BLUE"

pi = 3.14
print(str(pi)) # "3.14"

# dot notation (.upper(), .lower()) vs len(), str()
# Methods that use dot notation only work with strings
# len() and str() can work on other data types

# STRING CONCATENATION 
# + operator between strings will 'add' them together
print("Spam" + " and " + "eggs") # "Spam and eggs"

# EXPLICIT STRING CONVERSION
# to combine a string with something that isn't a string
# str() method converts non-strings into strings
# print("The value of pi is around " + 3.14) -> ERROR
print("The value of pi is around " + str(3.14)) # "The value of pi is around 3.14"

# STRING FORMATTING WITH % 
# useful when you want to print variables with strings
# the % operator will replace the %s in the string with the string variable that comes after it
# You need the same number of %s terms in a string as the number of variables in parentheses:
string_1 = "Camelot"
string_2 = "place"
print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)) # "Let's not go to Camelot. 'Tis a silly place."

# to pad integer variables with zeros: %02d instead of %s
# - 0 tells Python to pad with zeros
# - 2 pads to 2 characters wide
day = 6
print("03 - %02d - 2019" % (day)) # 03 - 06 - 2019

# DATETIME LIBRARY
from datetime import datetime

# get current date and time:
now = datetime.now()
print(now) # 2018-07-11 22:36:50.097711
print(now.year) # 2018
print(now.month) # 7
print(now.day) # 11

# printing in specific format:
print("%02d/%02d/%04d" % (now.month, now.day, now.year)) # 07/11/2018
print("%02d:%02d:%02d" %(now.hour, now.minute, now.second)) # 22:36:50

## CONDITIONALS AND CONTROL FLOW ##
# Control flow gives us this ability to choose among outcomes based on what else is happening in the program.
# Comparators: ==, !=, <, >, <=, >=





