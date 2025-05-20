import pandas as pd
from googleapiclient.discovery import build


apı='AIzaSyAW0yub2ubO2LJyUyAyts1--47tb2Um_2k'
# youtube api servisini başlatma 
youtube=build('youtube', "v3", developerKey=apı)

catogori= {
    "10": "Music",
    "17": "Sports",
    "20": "Gaming",
    "24": "Entertainment",
    "26": "Howto & Style"
}
with pd.ExcelWriter("youtube_cato.xlsx", engine="openpyxl")as writer:

  for cato_id ,cat in catogori.items():
  
     reques=youtube.videos().list(
         part="snippet,statistics",
         chart="mostPopular",
         regionCode="TR",
         videoCategoryId=cato_id,
         maxResults=30
     )

response=reques.execute()
yt=[]
print("video başlıkları")
for video in response['items']:
    print(video['snippet']['title'])
    print(video['statistics'])


    ddvideo={
        "catogori":cat,
        "Title":video['snippet']['title'],
        "Date":video['snippet']['publishedAt'],
        "liveBroadcastContent":video['snippet']['liveBroadcastContent'],
        "Channel":video['snippet']['channelTitle'],


        "Comment":video['statistics']['commentCount'],
        "View":video['statistics']['viewCount'],
        "Like":video['statistics']['likeCount']

   
    }
    yt.append(ddvideo)
    dataf=pd.DataFrame(yt)
     
    dataf.to_csv("youtube_data.csv", index=True,encoding="utf-8-sig" )
  



    


