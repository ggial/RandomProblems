#!/usr/bin/env python
# coding: utf-8

# # MASTERMIND
# A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”.

# ## Import libraries

# In[39]:


import random


# Main function

# In[40]:


def main():
    
    print("Do you want me to explain the rules of the game?")
    ans = input()
    if ans=="Yes" or ans=="YES" or ans=="yes":
        ExplainRules()
    
    PIN = SetPin()
    
    LetUserGuess(PIN)
    
    
    return


# Creating a random 4-digit PIN code

# In[41]:


def SetPin():
    PIN = ""
    for i in range(4):
        PIN+=str(random.randint(0,9))
    return PIN


# User guessing the PIN

# In[1]:


def LetUserGuess(PIN):
    Attempt = 1
    while Attempt<=10:
        print("You are on attempt #" +str(Attempt) +".")
        Out = ""
        Guess = input('Enter your guess: ')
        for i in range(4):
            if Guess[i] not in PIN:
                Out+="B"
            elif Guess[i]==PIN[i]:
                Out+="R"
            else:
                Out+="Y"
        if Out=="RRRR":
            print("YE BOI! YOU DID IT!")
            print("No one cares really, but gj, you won.")
            print("The code " +PIN +" was correct")
            input()
            return
        else:
            print(Out)
            if Attempt<9:
                print("You have " +str(10-Attempt) +" attempts left mate.")
            elif Attempt == 9:
                print("Ready for your last attempt mate?")
            else:
                print("Sorry mate, you bad.")
                print("PIN was " +PIN)
                print("LOSER")
                input()
        Attempt+=1
    return


# Explain Rules

# In[43]:


def ExplainRules():
    
    print("Alright mate, here goes nothing. Listen up.")
    print("A 4-digit PIN code is randomly generated. You have to guess it within 10 attempts. Alright?")
    ans = input()
    print("Don't care. Listen, you will be guessing 4-digit codes.")
    print("If a digit does not exist at all in the PIN, you'll get a 'B' at its place. Good so far?")
    ans = input()
    print("If a digit exists in the PIN, but you placed it in the wrong place, you'll get a 'Y' at its place. Good?")
    ans = input()
    print("Finally, if you guess a digit in its correct place, you'll get an 'R' at its place.")
    print("You got it? Do you want an example?")
    ans = input()
    if ans == "yes" or ans == "YES" or ans == "Yes":
        Example()
    else:
        print("Good luck with your game.......")
    ans = input()
    return


# Example for explain rules function

# In[44]:


def Example():
    
    print("Pff....")
    ans = input()
    print("Fine, let's get this over with.")
    print("Assume the generated PIN is '1234'.")
    print("if you guess '5678' you'll get back 'BBBB', because all the digits were wrong. Fine?")
    ans = input()
    print("If you guess '0100' you will get back 'BYBB', because 1 exists in the PIN code, but in a different position.")
    ans = input()
    print("If you guess '1325' you will get back 'RYYB'.")
    print("I hope you get why. Do you?")
    ans = input()
    if ans == "NO" or ans =="No" or ans == "no":
        Example()
    
    print("Right, good luck...")
    ans = input()
    return


# In[48]:


main()


# In[ ]:




