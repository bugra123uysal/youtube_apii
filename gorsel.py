import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

url=pd.read_excel("C:\\Users\\buğra\\Desktop\\youtube_data.xlsx")

print(url.columns)

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
 
