#Lists

#Lists are ordered, mutable and allow duplicate values

# coaches_lists = ["Callum", "Adian", "Sandra", "Remi", "Kaki","Ronnie"]
# print(len(coaches_lists))
#
# #List indexing
# print(coaches_lists[2])
#
# #up to 3rd element
# print(coaches_lists[:3])
#
# # star at index 2 onwards
# print(coaches_lists[2:])
# print(coaches_lists[1:3])
#
# # returns a bool
# print("Kaki" in coaches_lists) # True
#
# #Change an item in a list
# coaches_lists[1] = "Bob"
# print(coaches_lists)
#
# # Change list with multiple items
# coaches_lists[1:3] =["George", "John"]
# print(coaches_lists)
#
#
# #Nagetive indexing
# print(coaches_lists[-1])
#
# #using str
# x="cool"
# print(x[-1])
#
# num_list = [1,2,3,4,5]
# #insert  a values
# num_list.insert(2, 250)
# print(num_list)
#
# #remove the last item in the list
# num_list.pop()
# print(num_list)
#
# #remove the specific index valus
# num_list.pop(1)
# print(num_list)
#
# #sort the list
# num_list.sort(reverse=True)
# print(num_list)


# Add to the end of the list
# num_list.append(255)
# print(num_list)

##SLicing
my_list = [10,20,30,40,50,60,70]

#negative slicing
print(my_list[-7::3])

# Syntax: List[Initial : End : IndexStep ]
# Slice returns portion of List from Initial to End at the step size of IndexStep
# Slicing can be done on lists, strings, and tuples

#Arrays
import array as arr
#making an array, the "i" is to declare the data type of the array -- >integer

num_arr1 = arr.array('i', [1,2,3,4,5,6,7,8,9,10])
print(type(num_arr1))   # <class 'array.array'>

print(type(arr))#casting  a list to an array
num_list2 =[1,2,23,3,22]

num_arr = arr.array('i', num_list2)
print(type(num_arr))

#Slicing arrays
print(num_arr[2:5])
print(num_arr[:5])
print(num_arr[:-4])


#Changing elements in an array
num_arr[0] =1
print(num_arr)
num_arr[2:5] = arr.array('i',[5,6,7])
print(num_arr)

#concatenation
to_five = arr.array('i', [1,2,3,4,5])
to_ten = arr.array("i", [6,7,8,9,10])

numbers =arr.array("i") #make an empty array
numbers = to_five + to_ten
print(numbers)
#delete an element
del numbers[2]
print(numbers)

#Arry methods
nums = arr.array("i", [1,2,3,4,5])

#append
nums.append(4444444)
print(nums)

#extend()
nums.extend([5,6])
print(nums)

#pop()
nums.pop()
print(nums)
nums.pop(2)
print(nums)

#array method, count() -count the number of times a number occurs in an array
num_nums = arr.array("i", [1,2,2,3,4,5])
print(num_nums.count(3)) #1
print(num_nums.count(2)) #2

#Go over anything you need to from todays sessions
# Look into iter() and next(), what do they do regarding arrays?
# Create a multiplication table for the 5X table using only lists and list methods (no loops)
# Find and print the following
# Print the full list
# Remove one value from the list
# insert a number back in the correct place
# Remove the last value
# Print the 5th element
# Find the position of 40 in the list
# Count how many times 5 appears in the list

# Step 1: Start with an empty list

times_five = []

# Step 2: Use append to build the list step by step

times_five.append(5 * 0)
times_five.append(5 * 1)
times_five.append(5 * 2)
times_five.append(5 * 3)
times_five.append(5 * 4)
times_five.append(5 * 5)
times_five.append(5 * 6)
times_five.append(5 * 7)
times_five.append(5 * 8)
times_five.append(5 * 9)
times_five.append(5 * 10)


# Step 3: Print the full list

print(times_five)

#remove a number
times_five.pop(-2)
print(times_five)

#insertback the number
times_five.insert(-1, 45)
print(times_five)

# remove the last number
times_five.pop()
print(times_five)

# Print the 5th element
print(times_five[4])

## Find the position of 40 in the list
pos_40 = times_five.index(40)
print("index of 40 : ",pos_40)


#Count how many times 5 appears in the list
count_5 = times_five.count(5)
print("count of 5: ",count_5)