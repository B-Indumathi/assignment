#!/usr/bin/env python
# coding: utf-8

# In[20]:


# 11 question
'''Write a function called show_stars(rows). If rows are 5, it should print the following:
*
**
***
****
*****'''


def show_stars(rows):

    for i in range(0, rows+1):
            for j in range(i):
                print("*",end="")
            print(" ")
show_stars(5)


# In[10]:


# 13 question
#  Iterate the given list of numbers and print only those numbers which are divisible by 5
l1 = [1,25,32,310,465] 
for i in l1:
    if i%5 == 0:
        print(i)


# In[11]:


#14 question
# Write a program to find how many times substring “hi” appears in the given string.

s ="hihellohihihiwelhi"
print(s.count("hi"))


# In[24]:


# 15 question
'''Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''
n = 5;
for i in range(0, n+1):
        for j in range(i):
            print(i,end=" ")
        print(" ")


# In[26]:


#list problems
#Python program to interchange first and last elements in a list
myList = [1, 23, 3, 45, 43, 98]
print("List before swapping:",myList)
l = len(myList)
myList[0],myList[-1]= myList[-1],myList[0]

print("List after Swapping : ", myList)


# In[33]:


#Python program to swap two elements in a list
myList = [1, 23, 3, 45, 43, 98]
print("List before swapping:",myList)
l = len(myList)
pos1 = int(input("enter which place it has to be replaced "))
pos2 = int(input("enter which place it has to be replaced:"))
myList[pos1],myList[pos2]= myList[pos2],myList[pos1]

print("List after Swapping : ", myList)


# In[32]:


#Python | Ways to find length of list
myList = [1,2,3,4,5,6,7,8]
l= len(myList)
print("length of the list using len function",l)
count = 0
for i in myList:
    count = count +1;
print("length of the list using for loop",count)


# In[34]:


#Maximum of two numbers in Python
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
  
m = max(a, b)
print("the maximum element using inbuilt function:",m)
      #or
if (a> b):
    print("the maximum element using if loop",a)
else:
    print("the maximum element using if loop",b)


# In[35]:


#Minimum of two numbers in Python
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
  
m = min(a, b)
print("the minimum element using inbuilt function:",m)
      #or
if (a> b):
    print("the minimum element using if loop",b)
else:
    print("the minimum element using if loop",a)


# In[40]:


# Tuple problems
#Python program to Find the size of a Tuple
import sys
tup= ((1, 2), (4, 6), (7, 2), 10.9,"hello")

print("Size of tuple: ", sys.getsizeof(tup), "bytes")


# In[41]:


#Python – Maximum and Minimum K elements in Tuple
def Findel(tup,K):
    result = []
    test_tup = list(tup)
    temp = sorted(tup)
    for i, val in enumerate(temp):
        if i < K or i >= len(temp) - K:
            result.append(val)
    result = tuple(result)
    # printing result 
    print("Max and Min K elements : ",result)

tup = (13, 10, 23, 2, 5, 6, 12)
K = 2
print("The original tuple: ", tup)
Findel(tup,K)


# In[43]:


#Python – Sum of tuple elements
tuple1 = (7, 8, 9, 1, 10, 7) 
print("The original tuple is : " ,tuple1) 
sum = 0;
for i in tuple1:
    sum = sum+ i
  
print("The summation of tuple elements are : ",sum) 


# In[48]:


#string problems
#Python program to check whether the string is Symmetrical or Palindrome
def check_palindrome(my_str):
    mid_val = (len(my_str)-1)//2
    start = 0
    end = len(my_str)-1
    flag = 0
    while(start<mid_val):
        if (my_str[start]== my_str[end]):
            start += 1
            end -= 1
        else:
            flag = 1
            break;
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
def check_symmetry(my_str):
    n = len(my_str)
    flag = 0
    if n%2:
        mid_val = n//2 +1
    else:
        mid_val = n//2
    start_1 = 0
    start_2 = mid_val
    while(start_1 < mid_val and start_2 < n):
        if (my_str[start_1]== my_str[start_2]):
            start_1 = start_1 + 1
            start_2 = start_2 + 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
my_string = 'phphhphp'
check_palindrome(my_string)
check_symmetry(my_string)


# In[60]:


#Reverse words in a given String in Python
string = "geeks quiz practice code"
s = string.split(' ')
print(s)
print("reversed string:"," ".join(s[::-1]))


# In[62]:


#Ways to remove i’th character from string in Python
s1 = str(input("enter the string:"))
print ("The original string is : " ,s1)
pos = int(input("enter the index value which has to be removed:"))
new_str = ""
  
for i in range(len(s1)):
    if i != pos:
        new_str = new_str + s1[i] 
print ("The string after removal of i'th character : " , new_str)


# In[64]:


# set problems
# Find the size of a Set in Python
set1 = {"gaja",1,"100",(1,23,3)}
print("Size of Set: " , str(set1.__sizeof__()) , "bytes")


# In[65]:


#Iterate over a set in Python
set1 = {"gaja",1,"100",(1,23,3)}
for i in set1:
    print(i)


# In[67]:


# Dictionary problems
# Python | Sort Python Dictionaries by Key or Value
names = {'alice':1,'sundar':5,'Peter':3 ,'Andrew':9 ,'Ruffalo':78 ,'Chris':90 } 
print(sorted(names.keys()))   
print(sorted(names.items()))  


# In[68]:


#Python dictionary with keys having multiple inputs
my_dict = {}

a, b, c = 15, 26, 38
my_dict[a, b, c] = a + b - c

a, b, c = 5, 4, 11
my_dict[a, b, c] = a + b - c

print("The dictionary is :")
print(my_dict)


# In[69]:


# function problems
# How to get list of parameters name from a function in Python

def dip(a, b):
    return a**b
import inspect
print(inspect.signature(dip)) 


# In[71]:


# How to Print Multiple Arguments in Python
def GFG(name, no):
    print("Hello from ", name, ', ', no)
GFG("ilaikiya", "18")


# In[74]:


# Matrix problems
#Adding and Subtracting Matrices in Python
import numpy
A=[ [2, 3, 4], [3, 4, 5], [7, 7, 0] ]
B=[ [5, 6, 7], [1, 9, 3], [8, 6, 8] ]

print("Addition of two matrices are: ")
print(numpy.add(A,B))
print("subtraction of two matrices are:")
print(numpy.subtract(A,B))


# In[ ]:





# In[ ]:




