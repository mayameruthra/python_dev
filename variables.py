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
census=["households",100,"farm_produce",{"sex":"female","gas":"ola_energy"}]
print(census)
# census contain data types such as dictionary, string,list
# my info contain all data types including a list, dictionary,strings

# tuple: An immutable (unchangeable) ordered sequence of items. Similar to lists but cannot be modified.
# once created added, removed or changed
coordinates = (10.0, 20.0)  # tuple
empty_tuple = ()  # tuple
my_tuple=(1,"hello",3.13)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
mixed=('maya','ali',22)
print(mixed)
print(mixed[0])
print(mixed[1])

# range: Represents an immutable sequence of numbers, typically used in loops.
r = range(10)  # range from 0 to 9
# The range() function can be called in three different ways:


# range(stop): Generates numbers from 0 to stop - 1.
# range(start, stop): Generates numbers from start to stop - 1.
# range(start, stop, step): Generates numbers from start to stop - 1, incrementing by step. If step is negative, it decrements
for index in range(7):
    print(index) #this print from 0 to 6
    for index in range(10):
        print(index)

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

# # 5.binary types
# Binary types in Python are used to work with binary data (i.e., data represented in terms of bytes, rather than human-readable text).
#  These types are useful when dealing with files, data streams, network protocols, or encoding/decoding operations.

# 1. bytes: Immutable Sequence of Bytes
# What it is: The bytes type is a sequence of immutable 8-bit values (ranging from 0 to 255). 
# It is often used to represent binary data, such as files, network data, or images.

# Usage: Once created, a bytes object cannot be modified (i.e., it's immutable).

# Example:
b = b"hello"  # Create a bytes object
print(b)  # Output: b'hello'
print(b[0])  # Output: 104 (ASCII value of 'h')
print(b[1])

# bytearray: Mutable Sequence of Bytes
# What it is: The bytearray type is similar to bytes, but unlike bytes, it is mutable.
# #  You can modify its contents after creation. It's useful when you need to manipulate byte sequences, such as editing binary data in files.

# Usage: You can change individual bytes in a bytearray, unlike with bytes.

# Example:
ba = bytearray(b"hello")  # Create a mutable bytearray from a bytes object
print(ba)  # Output: bytearray(b'hello')

ba[0] = 72  # Modify the first byte (ASCII value of 'H')
print(ba)  # Output: bytearray(b'Hello')

# memoryview: Memory View of Binary Data
# What it is: A memoryview object allows you to work with memory buffers (like bytes or bytearray) without making a copy of the data.
#  It exposes a view of the original binary data, meaning you can work with slices of data efficiently.

# Usage: This is useful when you need to manipulate large binary datasets, such as streaming data,
#  without copying the entire dataset into memory.

# Example:
mv = memoryview(b"hello")  # Create a memory view from a bytes object
print(mv[0])  # Output: 104 (ASCII value of 'h')

# Slice the memory view (works like slicing an array)
print(mv[1:3].tobytes())  # Output: b'el' (extract a part of the original bytes object)



# 6.none types
# 7.callabale types
# function: A user-defined function that can be called with arguments and return values.
def print_name():
    return {'coutry':'kenya','age':23}
print(print_name()) 

# lambda function uses lambda key words
# A lambda function to add two numbers
add = lambda x, y: x + y

# Call the lambda function
result = add(3, 5)
print(result)  # Output: 8

subtract=lambda w,r:w-r
result_1=subtract(10,5)
print(result_1)


# 8.iterator types


