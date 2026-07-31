firstname = input("Enter your first name: ")
lastname = input("Enter your second name: ")

print(len(firstname))
print(type(len(firstname)))
print(f'My name is {firstname} {lastname} and my age is 23')

s = firstname[1:4]
#last one is excluded
# negative also form -1 from last char [start: stop: step]
# step means jump by default it is 1
# reverse [::-1]
#[].upper() also valid lower(), len

s1 = firstname[::-1]
print(s1)
print(firstname.upper())
print(firstname.lower())

# Built in Functions in python

#len(), title() ----> every word first letter of sentence is Capital and rest are in lower case
#count(string, start index for search, end index for search) By default it is 0 to n - 1
#find(str, start,end)--> will the start index of substring and if it is not find then it will return -1
# index() is same as find but will return error if given string is not found the string in which we are looking for
#endswith("World!") is it endswith then it will return true otherwise it will return false
#startswith() similar like endswith
#isalnum() to check whether the string contain only number and char if yes then it will return true otherwise it will return false
# islower() if contains all lower case + any other thing
# is upper() --> similar to islower()
# istitle()
# strip() to remove extra space in both sides-->lstrip() for left and rstrip for right side
#replace(oldstr, newstr)
#split() return list of words we can also mention split('a')
