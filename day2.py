#functions
#blocks of code that are reusable
#DRY , dont repeat yourself
#can return data in order to get it out of the function
#in python we use the def keyword
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
def circle(radius):
    return 2 * 3.14 * radius

circleA = circle(2)
sumb = sum(2,3)
print(sumb)
print(circle(2))