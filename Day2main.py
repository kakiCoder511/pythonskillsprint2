#regular function
from xml.dom.expatbuilder import theDOMImplementation


def sum(a,b):
    return a + b

#lamba function
sum_lambda = lambda a, b: a + b
print(sum(1,2))
print(sum_lambda(1,2))

#Challenge
# Convert the following functions to lambda expressions:

import math

def circle_perimeter(radius):
    return 2 * math.pi * radius

#into Lambda
circle_perimeter_lambda = lambda  radius: 2 * math.pi * radius
print(circle_perimeter_lambda(2))

def circle_area(radius):
    return math.pi * radius ** 2

#into Lambda
circle_area_lambda = lambda radius: math.pi * radius ** 2
print(circle_area_lambda(2))

#Bonus challenge - convert to Lambda 🤯

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

triangle_area_lambda = lambda a, b, c: math.sqrt(
    ((a + b + c) / 2)
    * (((a + b + c) / 2) - a)
    * (((a + b + c) / 2) - b)
    * (((a + b + c) / 2) - c)
)

print(triangle_area_lambda(3, 4, 5))  # 6.0


#lambda functions in practice
# map & filter
add = lambda x, y: x + y
print(add(1, 2))

subtract = lambda x, y, z: x + y -z
print(subtract(2,3,2))

cube = lambda x: x ** 3
print(cube(3))

#1.lambda inside a function
def multiplier(n):
    return lambda x: n * x

doubler = multiplier(2)
triple =multiplier(3)

print(f"doubler : {doubler(3)}")
print(f"doubler : {triple(3)}")

#2. lambda function with Map and Filter
# map - apply a function to  each element

numbers =[2,3,4,5]
doubled =list(map(lambda x :x *2, numbers))
print(doubled)

#filter - apply a condition to each element to filter them
numbers = range(1,10)
evens = list(filter(lambda x : x % 2 == 0, numbers))
odds = list(filter(lambda x : x % 2 == 1, numbers))
print(evens)
print(odds)

#sort
numbers =[100,6,2,3,4,5]
abc = ["m", "s", "s", "w", "e", "f", "f"]

sort_num= list(sorted(numbers, reverse =True))
sort_abc =list(sorted(abc))
sort_mod3 = list(sorted(numbers, key=lambda x: x % 3))

print(sort_num)
print(sort_abc)
print(f"sort_mod3: {sort_mod3}")

#reduce
#syntax reduce(function, iterable[, initializer])
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)


