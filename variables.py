# a variable name is an identity for data store
# 1.numeric types

# int (Integer): Whole numbers, positive or negative, without decimals.
x = 5  # int
y = -100  # int
z=50
print(z)

# float (Floating-point number): Numbers with decimal points.
pi = 3.14  # float
temp = -273.15  # float
time=4.5
print(time)



# 2.sequence type

# str (String): A sequence of characters enclosed in quotes (single, double, or triple).
name = "Alamin"  # str
sentence = 'Python is awesome!'  # str
first_name="maya"
print(first_name)
my_sentence="i love my man"
print(my_sentence)

# list: A mutable (changeable) ordered sequence of items. Elements can be of mixed data types.
fruits = ['apple', 'banana', 'cherry']  # list
mixed_list = [1, "hello", 3.5]  # list with mixed types
my_info=["maya",22,"kenya",{"country":"kenya","age":22},["kips",44]]
print(my_info)
# my info contain all data types including a list, dictionary,strings

# tuple: An immutable (unchangeable) ordered sequence of items. Similar to lists but cannot be modified.
# once created added, removed or changed
coordinates = (10.0, 20.0)  # tuple
empty_tuple = ()  # tuple
my_tuple=(1,"hello",3.13)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])

# range: Represents an immutable sequence of numbers, typically used in loops.
r = range(10)  # range from 0 to 9
# The range() function can be called in three different ways:

# range(stop): Generates numbers from 0 to stop - 1.
# range(start, stop): Generates numbers from start to stop - 1.
# range(start, stop, step): Generates numbers from start to stop - 1, incrementing by step. If step is negative, it decrements
for index in range(7):
    print(index) #this print from 0 to 6

# 3.set types
# A set is an unordered collection of unique elements in Python.
#  This means that each element in a set appears only once, and the order of elements is not preserved.
#   Sets are primarily used when you want to store items but do not want 
#   duplicates and don't care about the order of elements
unique_numbers={1,2,3,5,4}
print(unique_numbers)

# 4.mapping types
# dict (Dictionary): An unordered collection of key-value pairs.
#  Keys must be unique and immutable (strings, numbers, tuples), while values can be of any type.
kips_info={"country":"kenya","name":"maua"}
print(kips_info)
# 4.boolean types
# they can either be true or false
info_maya={"is_female":True,"is_married":False}
print(info_maya)
# 5.binary types
# 6.none types
# 7.callabale types
# 8.iterator types


