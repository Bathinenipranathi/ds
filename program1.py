#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
hours_studied=[10,9,2,15,10,16,11,16]
exam_scores=[95,80,10,50,45,98,38,93]
plt.plot(hours_studied,exam_scores,marker='*',color='red',linestyle='-')
plt.xlabel('Hours Studied')
plt.ylabel('Score in final exam')
plt.title("Effect of hours studied on exam scores")
plt.show()

