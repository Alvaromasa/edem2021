#!/usr/bin/env python
# coding: utf-8

# In[6]:


from vega_datasets import data
stocks = data.stocks()

import altair as alt
alt.Chart(stocks).mark_line().encode(
  x='date:T',
  y='price',
  color='symbol'
).interactive(bind_y=False)


# In[ ]:





# In[ ]:





# In[ ]:




