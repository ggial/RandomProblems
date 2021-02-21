#!/usr/bin/env python
# coding: utf-8

# # INFINITE MONKEY THEOREM
# 
# The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long would it take for a Python function to generate just one sentence? The sentence I will go for is: “i should be spending my time better”.
# 
# Found this problem at "https://www.geeksforgeeks.org/intermediate-coding-problems-in-python/"

# Note! I will asume that only lower case english letters can be typed by the monkey. 

# Possible improvements: 
# 1) Monkey can also type numbers, symbols, trigger capital letter etc.
# 
# 

# ## Import Libraries

# In[49]:


import random
import time


# ## Start defining functions

# Main Function

# In[66]:


def main():
    # Define a char array with all possible symbols the monkey could type
    PossibleSymbols = "abcdefghijklmnopqrstuvwxyz "
    #State the sentence we seek for the monkey to type
                                                            #DesiredSentence = "ab" test
    DesiredSentence = "love you"
    # DesiredSentence = "i should be spending my time better" takes too much time
    #Initialize monkey text to blank
    MonkeyText = ""
    
    while DesiredSentence not in MonkeyText:
        MonkeyText+=MonkeyType(PossibleSymbols)
    
    print(MonkeyText)
    return


# Function: monkey pressing 1 button

# In[67]:


def MonkeyType(PossibleSymbols):
    
    r = random.randint(0,len(PossibleSymbols)-1)
    
    return PossibleSymbols[r]


# Main Function Call

# In[ ]:


start = time.time()
main()
end = time.time()
print("Time elapsed was: " + str(end - start) +" seconds")


# In[ ]:




