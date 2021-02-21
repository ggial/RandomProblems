#!/usr/bin/env python
# coding: utf-8

# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.
# 
# The function should return 0 if a non-integer is passed in.

# In[13]:


def main():
    num = input()
    num = float(num)
    add_it_up(num)
    return


# In[18]:


def add_it_up(num):
    sum = 0
    if num == int(num):
        for i in range(int(num)+1):
            sum = sum + i
    print(sum)
    return


# In[22]:


main()

