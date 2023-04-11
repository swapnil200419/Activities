"""
Complete the Exercises - Representing Abstraction Through Code In programming, we deal with two kinds of elements: functions and data.
Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data.
By the concept of abstraction create functions representing abstracting principles through function
Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function. Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3) Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3) Factor: Calculate temperature that a person feels because of the wind (Python3) Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use function_factor.py"""

a=int(input())
b=int(input())
def add(a,b):
    c=a+b
    return c
print("Addition:",add(a,b))
def subtract(a,b):
    c=a-b
    return c
print("Subtraction:",subtract(a,b))
def multiply(a,b):
    c=a*b
    return c
print("Multiplication:",multiply(a,b))
def divide(a,b):
    c=a/b
    return c
print("Division:",divide(a,b))
def power(a,b):
    c=a**b
    return c
print("Power:",power(a,b))
def remainder(a,b):
    c=a%b
    return c
print("Remainder:",remainder(a,b))
def float_division(a,b):
    c=a+b
    return c
print("Float division:",float_division(a,b))