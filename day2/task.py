""" TypeError
These errors occur when you are using the wrong data type. e.g. len(12345)

Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

PAUSE 1. Fix the len() function so it has no more warnings or errors.
Type Checking
You can check the data type of any value or variable in python using the type() function.

print(type("abc")) #will give you <class 'str'>

PAUSE 2. Write out 4 type checks to print all 4 data types
Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>

Type Conversion
You can convert data into different data types using special functions. e.g.

float()

int()

str()

PAUSE 3. Make this line of code run without errors
print("Number of letters in your name: " + len(input("Enter your name"))) """
print("Number of letters in your name: " + str(len(input("Enter your name "))))

""" Basic Operators
Learn to use the basic mathematical operators, +, -, *, /, // and **

PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

PAUSE 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)

PAUSE 2. Change the code so it outputs 3?
print(3 * 3 + 3 / 3 - 3) """

print("My age: " + str(12))
print(3 * 3 + 3 / 3 - 3)
print(int(3*3+3/3-7))

"""
Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

int(3.738492) # Becomes 3

Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14

Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

+=

-=

*=

/=

f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")

Will output I am 12 years old.
"""
bmi = 86 / 1.87 ** 2

print(f"My bmi is {int(bmi)}")

"""
We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60

Demo
https://appbrewery.github.io/python-day2-demo/

Very Optional Reading: Floating Point Arithmetic
https://docs.python.org/3/tutorial/floatingpoint.html

"""


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip / 100)
paid = total_bill / people

print(f"Each person should pay: ${paid:.2f}")

