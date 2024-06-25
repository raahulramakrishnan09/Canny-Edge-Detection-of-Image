#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[3]:


image=cv2.imread('Dodge_Charger.jpg')
gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[4]:


edge=cv2.Canny(gray_scale,50,150)


# In[5]:


cv2.imshow('original',image)
cv2.imshow('edge',edge)


# In[9]:


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




