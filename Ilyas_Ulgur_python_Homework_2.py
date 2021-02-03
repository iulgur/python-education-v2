#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Create a List and swap the second half of the list with the first half of the list and print this list on the screen
#define a list
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
# Create list1 with half elements (first 5 elements)
list1 = list[:5]
print(list1)
# Create list2 with next half elements (next 3 elements)
list2 = list[5:]
print(list2)
list = list2 + list1
print(list)


# In[7]:


#2.	Ask the user to input a single digit integer to a variable ‘n’. 
#Then, print out all of the even numbers from 0 to n (including n)

# Python program to print Even Numbers in given range 
  

n = int(input("Enter a single digit integer number: ")) 
  
# iterating each number in list 
for i in range(0, n + 1): 
      
    # checking condition 
    if i % 2 == 0: 
        print(i, end = " ") 


# In[ ]:




