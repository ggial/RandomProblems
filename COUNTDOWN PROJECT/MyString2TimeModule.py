#!/usr/bin/env python
# coding: utf-8

# Import Relevant Libraries

# In[ ]:


import time


# Define Relevant Functions

# In[25]:


def string2time(t):
    if not t:
        print("Sorry My Lord, this is empty, my weak brain does not understand what it should do with it I deserve punishment")
        return ['Try','again','bro']
    if ":" in t:
        hours, mins, sec = t.split(":")
        return [hours, mins, sec]
    h,t = FindHours(t)
    m,s = FindMinsAndSecs(t)
    return [int(h),int(m),int(s)]
        


# In[26]:


def FindHours(t):
    if "hours" in t:
        h,t = t.split("hours")
    elif "hour" in t:
        h,t = t.split("hour")
    elif "hrs" in t:
        h,t = t.split("hrs")
    elif "hrs" in t:
        h,t = t.split("hrs")
    elif "h" in t:
        h,t = t.split("h")
    else:
        h = '0'
    return [h,t]    


# In[29]:


def FindMinsAndSecs(t):
    # Find minute value
    if "mins" in t:
        m,t = t.split("mins")
    elif "minutes" in t:
        m,t = t.split("minutes")
    elif "min" in t:
        m,t = t.split("min")
    elif "minute" in t:
        m,t = t.split("minute")
    elif "m" in t:
        m,t = t.split("m")
    else:
        m = '0'
    # Find seconds value
    if not t:
        s = '0'
    elif "seconds" in t:
        s,t = t.split("seconds")
    elif "second" in t:
        s,t = t.split("second")
    elif "sec" in t:
        s,t = t.split("sec")
    elif "s" in t:
        s,t = t.split("s")
    elif "secs" in t:
        s,t = t.split("secs")
    else:
        s = '0'     
    return [m,s]    

