my_name = "KLEIN"
print(my_name)
print(f"Hello, my name is {my_name.lower()}")

dog_name = "lucy"
print(f"Say hi to {dog_name.upper()}")

sister_name = "wendy"
print(f"{sister_name.capitalize()} can be annoying" )

print(type(dog_name))

print(int(4 / 3))
print(float(4 / 3))

# any set of comma separated data enclosed in a brackets is a list.
# [1, 3 400, 7] --> this is a list

print(list('abcde'))
print(list( (1, 2, 3) ))
print(list()) # for this an empty list is created. This happens with the list method when no argument is passed.

list_abc = list('abc')
print(list_abc) # expected output is all the three letters
print(list_abc[0]) # expected output is a only since it is the character at index 0
print(list_abc[1]) # expected output is b only since it is the character at index 1
print(list_abc[2]) # expected output is c only since it is the character at index 

print(len([1, 3, 4, 5, 6, 7])) #the len() method checks the length of a list by counting the number of characters.
print(sorted([2, 400, 1, 59, 68, 89])) # the sorted() method arranges the items in a list in the correct order

#  there is another data type similar to lists but enclosed data with brackets() called Tuple
print(tuple([1, 2, 3]))
print(tuple(list_abc)) # we have passed list_abc which was a list now converted it to a tuple changing this [] to this ()

 # tuples are less flexible than lists and are mostly used in databases since you want to keep acurate data

print(set(list_abc))
# set method --> This encloses data in parentheses {} and it can only take a list or tuple as an argument

print(set([1, 3, 5, 6, ])) # here the [] has been changed to {}
print(set((1, 3, 5, 6, ))) # here the () has been changed to {}

my_dict = {"name": "Klein", "second_name":"Kiuvu" ,"position": 1}
print(my_dict)
print(my_dict.get("name"))
print(my_dict.get("position"))
print(my_dict.get("name") + " " + my_dict.get("second_name"))
print(my_dict["name"])

# You can use the get method or the bracket notation to get what you want from a dictionary(dict)

no_value = None
print(no_value)

# like in Javascript we also have booleans in python but they are more of bools than booleans which is basically a short form
print(type(True)) # has a class of bool
print(type(False)) # has a class of bool

print(not True) # --> this basically prints the english equivalent of not true which is basically false
print(not False) # --> this basically prints the english equivalent of not false which is basically true

