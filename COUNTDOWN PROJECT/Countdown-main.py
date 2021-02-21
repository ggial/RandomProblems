#!/usr/bin/env python
# coding: utf-8

# In[8]:


import MyString2TimeModule
import time
import webbrowser


# In[12]:


url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'
# url2 = 'https://dictionary.cambridge.org/dictionary/english/time-s-up'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
t = input("How much time should I countdown for you My Lord?")
h,m,s = MyString2TimeModule.string2time(t)
print("I will notify you when time is up My Lord, by playing your favorite song!")
time.sleep(360*h+60*m+s)
webbrowser.get(chrome_path).open(url)


# In[ ]:




