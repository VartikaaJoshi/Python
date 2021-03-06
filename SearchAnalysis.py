# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C5GMB9pjF2EFzZzz7HmHkm6RhoGlSWvF
"""

#Search Analysis
#1
!pip install pytrends
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
 
trends.build_payload(kw_list=["adidas india","adidas mask","adidas"])
data = trends.interest_by_region()
data = data.sort_values(by=["adidas india","adidas mask","adidas"], ascending=False)
data = data.head(15)
print(data)
 
data.reset_index().plot(x="geoName", y=["adidas india","adidas mask","adidas"],figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()
