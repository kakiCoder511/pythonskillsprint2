#functions
#blocks of code that are reusable
#DRY , dont repeat yourself
#can return data in order to get it out of the function
#in python we use the def keyword
import math
import string
from genericpath import samefile


def hello(name):
    return f'Hello {name}'

sam =hello("Sam")
kaki =hello("Kaki")
name3Liam= hello("Liam")

print(sam)

#Function challenge

#create 2 mathematical functions that perform some sort of task and take in arguments
# (e.g. a function that adds and a functions that does the sqrt, etc
def sum(a,b):
    return a + b

print(sum(2,3))
def circle(radius):
    return  3.14 * radius* radius

circleA = circle(2)
sumA = sum(2,3)

print(sumA)
print(circle(2))

#Challenge 1: My First Python Function
# Write a function called my_first_function.
# Your function should take in a string as an argument.
# It should print in the format: "I love {argument}!".
def my_first_function(favourite_color):
   return (f"I love {favourite_color}!")

print("Challenge 1: My First Python Function")
print(my_first_function("blue")
)
# Challenge 2: Tripler
#
# Write a function tripler().
# It should take in a number and return the number × 3.
# Print the results with three different arguments.

def tripler(number):
    return number * 3
print(" Challenge 2: Tripler")
print(tripler(2))
print(tripler(3))
print(tripler(4))

# Challenge 3: Greeter
#
# Write a function greet() that takes a name as a parameter.
# It should return "Hello, {name}!".

def greet(name):
    return f"Hello {name}"
print("Challenge 3: Greeter")
print(greet("Sam"))
print(greet("Kaki"))

# Challenge 4: Even or Odd?
#
# Write a function is_even() that takes a number as input.
# Return "Even" if the number is even, "Odd" if it’s odd.
def is_even(number):

   if number % 2 == 0: return "Even"
   else: return "Odd"

print("Challenge 4: Even or Odd?")
print(is_even(2))

# num = int(input("Please enter the number: "))
# print(is_even(num))


# Challenge 5: Word Multiplier
#
# Write a function repeat_word(word, times)
# It should return the word repeated times number of times.

def repeat_word(word, times):
    return word *times

print("Challenge 5: Word Multiplier")
print(repeat_word("Sam",5))


# Challenge 6: Factorial (Stretch)
# Write a function factorial(n) that calculates the factorial of n.
# Example: factorial(5) → 5 * 4 * 3 * 2 * 1 = 120.
import math
# def factorial(Stretch):
#     return math.factorial(Stretch)

def factorial(n):
  if(n==0):return 1
  else: return n * factorial(n - 1)

print("Challenge 6: Factorial (Stretch)")


print(f"math.factorial: {factorial(0)}")
print(f"math.factorial: {factorial(4)}")


#
# Challenge 7: Default Parameters
# Write a function power(base, exponent=2)
# By default, it should square the base.
# If an exponent is provided, use it instead.

def power(base, exponent=2):
    return base ** exponent
print("Challenge 7: Default Parameters")
print(f"Power of the base number: {power(2)}")
print(f"Power of the base number: {power(3)}")
print(f"Power of the base number: {power(4)}")