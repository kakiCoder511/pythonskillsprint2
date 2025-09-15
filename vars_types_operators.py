# Python Basics
from sys import getsizeof

## Variables

## Assigning values to variable

x = 10 # integer
name = "Kaki" # a string
Name = "capital sensitive" # a string
is_happy = True # a boolean

## Using variables
print(x, name, is_happy)
print("Hello", name)
print("Are you happy?", is_happy)

## Reassigning values
x = 20
print("Now x is:", x)

## Memory Concept
my_number =  5
print(my_number) #5

my_number = my_number + 3
print(my_number) # 8

favorite_food = "Tomato"
print(favorite_food)
print(favorite_food)
Birth_Year = 1900
print(Birth_Year)
print("I was born in ",Birth_Year, "and my favourite is ", favorite_food)
##import the Python library
import sys

##function
def getsizeof(number):
    number/1.5
##Activity
x=42
y=3.14
z="hello"
b=False

##printout Activities
print(x , type(x), sys.getsizeof(x))
print(y, type(y),sys.getsizeof(y))
print(z, type(z),sys.getsizeof(z))
print(b, type(b), sys.getsizeof(b))

#Casting (Type Conversion)

#Casting means changing one type to another
#you can convert between compatible type (*e.g int--> float , bool -->int)
#CANNOT (e.g"HELLO" -->INT)
#CASTING EXAMPLE
my_num = 5
my_float =float(my_num)
print(my_float)

my_str = "123"
my_int =int(my_str)
print(type(my_int))

# my_bad_str ="hello45"
# my_bad_int = int(my_bad_str)
# print(my_bad_int)

print(int(False)) #0
print(int(True)) #1

#user input
# my_num_input = int(input("Enter a number: "))
# print(type(my_num_input))
##Ask the user for their age, store it as an integer, and print "You are [age] years old.".
# Ask the user for a decimal number, cast it to a float, and print the result.
# ask_for_age = input("Age?")
# print(ask_for_age)
# ask_for_decimal= float(input("decimal number ?"))
# print(float(ask_for_decimal))
#
# dec_num = float(input("Enter a decimal number: "))
# print(dec_num)

# Arithmetic and Comparison operators


# Python uses standard mathematical operators:

# + (addition)

# - (subtraction)

# * (multiplication)

# / (division --> returns a float)

# % (modulus --> remainder)


# Comparison operators

# > (greater than)

# < (less than)

# >= (greater than or equal to)

# <= (less than or equal to)

# == (equal to)

# != (not equal to)

#Operators example
print(5+3) #8
print(5*3) #15
print(10%3)#1

#input example
# num_to_multiply = int(input("Please input a number to multiplay by 2: "))
# print(num_to_multiply*2)

#strings
str1 = "Hello"
str2 = "World"
print(str1, str2,str1,str2)
print(str1 + " " + str2)

#Write a program that asks the user for two numbers and prints their sum.
# Try using * with a string (e.g. "Hi" * 3). What happens?
# # Check if 10 is greater than 5 using a comparison operator.
# a = int(input("enter a first number: "))
# b = int(input("enter a  second number: "))
# print("The sum is ", a*b)
# greeting = "Hi"
# print(greeting*3)
# print("Hi"*3)

#Comparison
print(10<5) #Flase


# Challenge 1: Mixed Casting
#
# Use input() to grab a number value from the user and cast it to a float.
# Divide the new float by any number and cast the result to an int.
# Use input() to grab the name of a user and print "Hello [name]!".

user_num= float(input("Please enter a number: "))
int_num= int(user_num/5)
print(int_num)
user_name= (input("Please enter your full name: ").title())
print("Hello", user_name)


# Challenge 2: Rectangle Area
#
# Grab a number value height from the user and store it as an int.
# Grab a number value width from the user and store it as an int.
# Print the area of a rectangle using the provided height and width.

area_height = int(input("Please enter the height: "))
area_width = int(input("Please enter the width: "))
print("Area of rectangle: ", area_height * area_width)


test_git = input("Please enter your test git: ")
print(test_git)