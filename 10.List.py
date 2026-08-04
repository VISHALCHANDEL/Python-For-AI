# List in Python
# The data type list is an ordered sequence that is mutable and made up of one or more elements.
# A list can have elements of different data types, such as integer, float string, tuple or even another lis

# List Operations
# Concatenation
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 'vishal']

list3 = list1 + list2
print(list3)

# 2.Concatenation
list4 = ['Hello']
list4 = list4 * 5
print(list4)

# 3.Membership
list5 = ['Vishal', 'Amrit', 'Ravinder', 'Naman']
if 'Vishal' in list5:
    print("Yes vishal is present in list5")

# 4.Slicing
# starting index and ending index and jump
list6 = ['Varun', 'Nitin', 'Rahul', 'Prajwal']
list6 = list6[2:3]
print(list6)

# Imp -----> a[-2:] It will print last two items of array
# [::-1]means in reverse direction
# [:-3:-1] Imp
# [-3::-1]

# len()---
print(len(list5))
# list7 = list() --means empty list
# append()--->list1.append(50) or list1.append([50, 60])
# extend to insert multiple elements
# insert() insert element at a particular index in the list
list1.insert(2, 25);
# count() --> how many times any elements comes in the list
# index() --> return the index and first index of the element
# otherwise it will return the error
# remove() remove the given element from the list and if the element is present multiple times in the list then it will remove the first occurence of the element in the list
# pop() we will give the index here
# reverse()
# sort() sort(reverse = True)---> for descending order
# sorted() will give new list
# min, max, sum
