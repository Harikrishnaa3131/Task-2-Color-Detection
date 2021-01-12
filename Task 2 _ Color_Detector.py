#!/usr/bin/env python
# coding: utf-8

# # TASK 1-Color Detection
# #The Sparks Foundation
# #By:  Harikrishnaa S

# In[1]:


import cv2
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


img1_path = 'D:\img 1.jpg'
img2_path = 'D:\img 2.jpg'
csv_path = 'D:\colours.csv'


# In[3]:


img2 = cv2.imread(img1_path)
img1 = cv2.imread(img2_path)


# In[4]:


plt.figure(figsize=(20,10))


# In[5]:


plt.imshow(img1)


# In[6]:


grid_RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)


# In[7]:


plt.figure(figsize=(20,10))
plt.imshow(grid_RGB)


# In[8]:


index = ['colour', 'colour_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv("D:\colors.csv", names=index, header=None)


# In[9]:


clicked = False
r = g = b = xpos = ypos = 0


# In[10]:


def get_color_name (R,G,B):
    minimum = 1000
    for i in range (len(df)):
        d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i,'colour_name']
            
    return cname


# In[11]:


def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img1[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[12]:


cv2.namedWindow('Task 2')
cv2.setMouseCallback('Task 2', draw_function)


# In[13]:


while True:
    cv2.imshow('Task 2',img1)
    if clicked:
        cv2.rectangle(img1, (20,20), (600,60), (b,g,r), -1)
        
        text = get_color_name(r,g,b) + ' R  =' + str(r) + ' G = ' + str(g) + ' B = ' + str(b)
        
        cv2.putText(img1, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
        
    if cv2.waitKey(20) & 0xFF == 27:
            break
            
cv2.destroyAllWindows()


# In[ ]:


#THANK YOU


# In[ ]:




