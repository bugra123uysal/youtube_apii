import pandas as pd
from googleapiclient.discovery import build
import psycopg2
from sqlalchemy import create_engine



base=psycopg2.connect(
      host="localhost",
      port="5432",
      database="youtubeapii",
      user="postgres",
      password="4516"
      
)
conne=base.cursor()

e_gin=create_engine("postgresql://postgres:4516@localhost:5432/youtubeapii")

apı='AIzaSyAW0yub2ubO2LJyUyAyts1--47tb2Um_2k'
# youtube api servisini başlatma 
youtube=build('youtube', "v3", developerKey=apı)

catogori=[
     ('1','Film & Animation'),
     ('2', 'Autos & Vehicles'),
    ('10', 'Music'),
    ('17', 'Sports'),
    ('20', 'Gaming'),
    ('24', 'Entertainment'),
    ('25', 'News & Politics'),
    ('28', 'Science & Technology')]
countrys=['TR','US','GB','IN','DE']
yt=[]
for coun in countrys:

          
    for cato_id ,cat in catogori:
           
           
           reques=youtube.videos().list(
               part="snippet,statistics,contentDetails",
               chart="mostPopular",
               regionCode=coun,
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
                   "country":coun,
                   "Title":video['snippet']['title'],
                   "Date":video['snippet']['publishedAt'],
                   "Channel":video['snippet']['channelTitle'],
                   "Comment":video['statistics'].get('commentCount', None), 
                   "View":video['statistics'].get('viewCount', None),   
                   "Like":video['statistics'].get('likeCount', None)    ,
                   "Duration":video['contentDetails'].get('duration', None),
                
                  
                 
    
           
              
               }
               yt.append(ddvideo)
dataf=pd.DataFrame(yt)
     
dataf.to_excel("youtube_data.xlsx", index=True,engine='openpyxl' )
dataf.to_sql("youtubeapii", e_gin, if_exists="replace", index=False)
  
