#!/usr/bin/env python
# coding: utf-8

# In[25]:


def main():
    
    Phrase = input("What phrase do you want to be ciphered?")
    n = int(input("Places to be moved?"))
    
    CipheredPhrase = CaesarCipher(Phrase,n)
    
    print(CipheredPhrase)
    return


# In[26]:


def CaesarCipher(Phrase,n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    CipheredPhrase = ""
    for i in range(len(Phrase)):
        if Phrase[i] in alphabet:
            ind = alphabet.index(Phrase[i])
            if ind+n<25:
                CipheredPhrase += alphabet[ind+n]
            else:
                CipheredPhrase += alphabet[ind+n-26]
        elif Phrase[i] in ALPHABET:
            ind = ALPHABET.index(Phrase[i])
            if ind+n<25:
                CipheredPhrase += ALPHABET[ind+n]
            else:
                CipheredPhrase += ALPHABET[ind+n-26]
        elif Phrase[i] == " ":
            CipheredPhrase += " "
        else:
            print("This is a strange symbol, I cannot cipher it...")
            return "I do not understand you Lord."
    
    return CipheredPhrase


# In[27]:


main()


# In[ ]:




