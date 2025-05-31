import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

url=pd.read_excel("C:\\Users\\buğra\\Desktop\\youtube_data.xlsx")

print(url.columns)
"""
top_view=url.sort_values(by='View', ascending=False).head(10) 
sns.barplot(x='View',  y='Title',hue='country' , data=top_view)
plt.show()

bad_view=url.sort_values(by='View', ascending=True).head(10)


sns.barplot(x='View',y='Title', hue='country' ,data=bad_view )
plt.title("")
plt.show()



top_coment=url.sort_values(by='Comment', ascending=False).head(10)
sns.barplot(x='Comment',y='Title' , hue='country',data=top_coment )
plt.title("")
plt.show()
bad_coment=url.sort_values(by='Comment', ascending=True).head((10))
sns.barplot(x='Comment',y='Title' ,hue='country' , data=bad_coment )
plt.title("")
plt.show()

top_Like=url.sort_values(by='Like', ascending=False).head(10)
sns.barplot(x='Like', y='Title',hue='country', data=top_Like)
plt.title("a")
plt.show()

bad_Like=url.sort_values(by='Like', ascending=True).head(10)
sns.barplot(x='Like', y='Title',hue='country' ,data=bad_coment)
plt.title("a")
plt.show()




total_like=url.groupby('country')['Like'].sum().reset_index().sort_values(by='Like', ascending=False)
sns.barplot(x='country', y='Like' , data=total_like)
plt.title("View-Like")
plt.show()
total_coment=url.groupby('country')['Comment'].sum().reset_index().sort_values(by='Comment', ascending=False)
sns.barplot(x='country' , y='Comment' , data=total_coment)
plt.title("View-Comment")
plt.show()

total_view=url.groupby('country')['View'].sum().reset_index().sort_values(by='View', ascending=False)
sns.barplot(x='country',y='View', data=total_view)
plt.title("View-Duration")
plt.show()
"""
total_Channel_like=url.groupby("Channel")['Like'].sum().reset_index().sort_values(by='Channel', ascending=False).head(10)
sns.barplot(x='Channel', y='Like' , data=total_Channel_like)
plt.title("channel-like")
plt.show()

total_Channel_view=url.groupby("Channel")['View'].sum().reset_index().sort_values(by='Channel', ascending=False).head(10)
sns.barplot(x='Channel' , y='View', data=total_Channel_view)
plt.title("channel-view")
plt.show()

total_Channel_coment=url.groupby("Channel")['Comment'].sum().reset_index().sort_values(by='Channel', ascending=False).head(10)
sns.barplot(x='Channel', y='Comment' ,data=total_Channel_coment)
plt.title("channel-coment")
plt.show()
