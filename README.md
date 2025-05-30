# youtube api 
Bu projede, Python kullanılarak YouTube Data API üzerinden belirli ülke ve kategori bazlı video verileri çekidim. Toplanan veriler hem Excel dosyasına hem de PostgreSQL veritabanına kaydedtim. 
## python  kütüphaneleri
import pandas as pd
from googleapiclient.discovery import build
import psycopg2
from sqlalchemy import create_engine
##  YouTube API Kurulumu
apı='**********************'
youtube=build('youtube', "v3", developerKey=apı)

## 🔗 veri tabanına bağlanma 

base=psycopg2.connect(
      host="localhost",
      port="5432",
      database="youtubeapii",
      user="postgres",
      password="****"
      
)
conne=base.cursor()

e_gin=create_engine("postgresql://postgres:****@localhost:5432/youtubeapii")


##kategoriler 
     ('1','Film & Animation'),
     ('2', 'Autos & Vehicles'),
    ('10', 'Music'),
    ('17', 'Sports'),
    ('20', 'Gaming'),
    ('24', 'Entertainment'),
    ('25', 'News & Politics'),
    ('28', 'Science & Technology')]

## ülkeler 
'TR':Türkiye
'US'=Amerika birleşik devletleri
'GB'=İngiltere
'IN'=Hindistan
'DE'=Almanya

##veilerin kaydedilmesi
EXCEL DOSYASINA KAYDEDİLMESİ
dataf.to_excel("youtube_data.xlsx", index=True,engine='openpyxl' ) 
SQL VERİTABANINA KAYDEDİLMESİ
dataf.to_sql("youtubeapii", e_gin, if_exists="replace", index=False)






