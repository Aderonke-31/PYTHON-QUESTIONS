#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to print Prime Numbers between 100 and 200(Hint: For Loop)

# In[16]:


for num in range(100,200):
    if all(num%i !=0 for i in range (2,num)):
        print(num)


# In[17]:


sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]


# 2. Write a sort function to sort the elements in the list

# In[18]:


sorted ([24, 34, 22, 11, 29, 88, 35, 12, 18, 35, 29, 30, 23, 64, 33, 96])


# 3. Write a sorting function without using the list.sort function (descending order)

# In[19]:


data_list = ([24, 34, 22, 11, 29, 88, 35, 12, 18, 35, 29, 30, 23, 64, 33, 96])
new_list = []

while data_list:
    minimum = data_list[0] # arbitrary number in list
    for x in data_list:
        if x > minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
    
print(new_list)
        
        


# 4. Write a Python program to Print Fibonacci Series

# In[20]:


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
    
for i in range(0,12):
    print(F(i))


# 5. Write a python Program to a list in reverse

# In[21]:


values = [21, 1, 3, 4, 5, 7, 8, 9, 19, 34, 48, 50, 51]
values.reverse()
print(values)


# In[22]:


# Using list.reverse() to reverse a list in Python
values = [1, 2, 3, 4, 5]
values.reverse()
print(values)

# Returns: [5, 4, 3, 2, 1]


# 6. write a python to check whether a string is a palindrome or not (Hint: A Palindrome is a word, phrase, number or sequence of words that reads the same backwards as forward. e.g madam)

# In[23]:


# Python program to check
# if a string is palindrome
# or not

x = "malayalam"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")


# In[24]:


# Python program to check
# if a string is palindrome
# or not

x = "madam"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")


# 7. Write a python program to print set of duplicates in a list

# In[25]:


numbers = [1,2,3,4,4,5,5,6,6,1,9,7,9]
duplicates = [number for number in numbers if numbers.count(number) > 1]
unique_duplicates = list(set(duplicates))

print(unique_duplicates)


# In[26]:


# Finding Duplicate Items in a Python List
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]

duplicates = [number for number in numbers if numbers.count(number) > 1]
unique_duplicates = list(set(duplicates))

print(unique_duplicates)

# Returns: [2, 3, 5]


# 8. Write a Python Programming to print number of words in a given sentence

# In[31]:


s = 'I am having a very nice day.'
print(len(s.split()))


# In[28]:


s = 'unlimited grace to see me through the journey of life.'
print(len(s.split()))


# In[36]:


data_list = ([2, 4, 2, 11, 2, 8, 35, 12, 18, 35, 29, 30, 23, 64, 3, 96])
new_list = []

while data_list:
    minimum = data_list[0] # arbitrary number in list
    for x in data_list:
        if x > minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
    
print(new_list)


# In[37]:


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-1)
    
for i in range(0,12):
    print(F(i))
    
 



# 9. Write Python Programming to implement a Binary Search

# In[39]:


def binary_search(arr, a, low, high):

    # Repeat until low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if arr[mid] == a:
            return mid

        elif array[mid] < a:
            low = mid + 1

        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
a = 4
#printing the array
print("The given array is", arr)

#printing element to be found
print("Element to be found is ", a)

index = binary_search(arr, a, 0, len(arr)-1)

if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")


# In[40]:


# Iterative Binary Search Function method Python Implementation  
# It returns index of n in given list1 if present,   
# else returns -1   
def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial list1  
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 45  
  
# Function call   
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1") 


# In[ ]:


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper: # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x: # these two are the actual lines
                break      # you' re looking for
                lower = x
        elif target < val:
                upper = x
                
                
                
binary_search(1,5)   


# 11. Write a python program to plot a simple bar chart

# In[67]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = [[30, 25, 50, 20],
        [40, 23, 51, 17],
        [35, 22, 45, 19]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'grey', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'pink', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'y', width = 0.25)


# In[51]:


from matplotlib import pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
ax.hist(a, bins = [0,25,50,75,100])
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()


# In[57]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()


# In[68]:


import matplotlib.pyplot as ply
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = 'SQL', 'PYTHON', 'R', 'C++', 'JAVA'
Students = [30, 26, 40, 18, 32]
ax.bar(langs, students)
plt.show()


# 12. Write a Python Program to join two string (Hint: using join ())

# In[79]:


# String Concatenation
# join() method is used to combine the strings

str1 = "Tutorial"
str2 = "point"


# join() method is used to combine  
# the string with a separator Space(" ") 

str3 = s1 + s2
str4 = s1 +" "+ s2

print(str3)
print(str4)


# In[80]:


str1 ='Aderonke'
str2 ='Sholuke'

str3 = str1 + str2
str4 = str1+" "+str2

print(str3)
print(str4)


# 13. Write a Pyhton Program to extract digits from giving string

# In[83]:


# initializing string
test_string = "1w3e4r5t6y7u7i8i"

# printing original strings
print("The original string : " + test_string)

# using join() + isdigit() + filter()
# Extract digit string
res = ''.join(filter(lambda i: i.isdigit(), test_string))

# print result
print("The digits string is : " + str(res))


# In[84]:


# Extract digit string
# using join() + isdigit() + filter()
 
# initializing string
test_string = 'g1eeks4geeks5'
 
# printing original strings 
print("The original string : " + test_string)
 
# using join() + isdigit() + filter()
# Extract digit string
res = ''.join(filter(lambda i: i.isdigit(), test_string))
     
# print result
print("The digits string is : " + str(res))


# In[87]:


# Get the list of all numbers in a string 
import re
str = 'We live at 9-162 Malibeu. My phone number is 666688888.'
#search using regex
x = re.findall('[0-9]+', str)
print(x)


# 14. Write a Python Program to split using newline delimeter

# In[90]:


str1 = "Welcome\nto\nTutorialspoint"

print("The given string is")
print(str1)

print("The resultant string split at newline is")
print(str1.splitlines()
)


# In[92]:


# Specify a delimiter for the first parameter, sep
s_comma = 'one,two,three,four,five'

print(s_comma.split(','))
# ['one', 'two', 'three', 'four', 'five']

print(s_comma.split('three'))


# 15. Give a string as your input, delete any reoccuring character, and return the new string

# In[99]:


def deleteReoccuringCharacters(string):
    
    seenCharacters = set()
    outputString = ''
    for char in string:
        if char not in seenCharacters:
            seenCharacters.add(char)
        outputString += char
    return outputString

deleteReoccuringCharacters("mississippi") 


print("After removing duplicates: ",remove_duplicate(s))    


# In[97]:


from collections import OrderedDict

def remove_duplicate(s): 
    return "".join(OrderedDict.fromkeys(s))

# test
s="mississippi"
print(s)
print("After removing duplicates: ",remove_duplicate(s))


# In[ ]:




