import pandas as pd
from googleapiclient.discovery import build


apı='AIzaSyAW0yub2ubO2LJyUyAyts1--47tb2Um_2k'
# youtube api servisini başlatma 
youtube=build('youtube', "v3", developerKey=apı)

catogori=[('10','Music'),('17','Sports'),('20','Gaming'),('24','Entertainment')]

yt=[]
""" with pd.ExcelWriter("youtube_data.xlsx", engine='openpyxl')as writer: """
for cato_id ,cat in catogori:
       
       
       reques=youtube.videos().list(
           part="snippet,statistics,contentDetails",
           chart="mostPopular",
           regionCode="US",
           videoCategoryId=cato_id,
           maxResults=50
       )

       response=reques.execute()


       print("video başlıkları")
       for video in response['items']:
           print(video['snippet']['title'])
           print(video['statistics'])
       
           ddvideo={
               "catogori":cat,
               "Title":video['snippet']['title'],
               "Date":video['snippet']['publishedAt'],
               "Channel":video['snippet']['channelTitle'],
               "Comment":video['statistics'].get('commentCount', None), 
               "View":video['statistics'].get('viewCount', None),   
               "Like":video['statistics'].get('likeCount', None)    ,
               "Duration":video['contentDetails'].get('duration', None)
              
             

       
          
           }
           yt.append(ddvideo)
dataf=pd.DataFrame(yt)
     
dataf.to_excel("youtube_data.xlsx", index=True,engine='openpyxl' )
  
