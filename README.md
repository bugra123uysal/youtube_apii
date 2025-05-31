# 🎥 YouTube API Project

In this project, I used **Python** to retrieve video data from the **YouTube Data API** based on specific **countries** and **categories**. The collected data was saved both to an **Excel file** and a **PostgreSQL database**.

## 📁 Project Overview

- ✅ Extracts data from YouTube for specific countries and categories
- ✅ Stores data in both Excel and PostgreSQL
- ✅ Handles missing values
- ✅ Uses YouTube API for video metadata
- ✅ Categorizes and filters data efficiently

---
## data types
Unnamed: 0      int64
catogori       object
country        object
Title          object
Date           object
Channel        object
Comment       float64
View          float64
Like          float64
Duration       object

## Null Check

catogori       0
country        0
Title          0
Date           0
Channel        0
Comment       15
View           1
Like          59
Duration       0

## 🐍 Python Libraries Used

import pandas as pd
from googleapiclient.discovery import build
import psycopg2
from sqlalchemy import create_engine

##🔧 YouTube API Setup
api_key = '**********************'
youtube = build('youtube', 'v3', developerKey=api_key)

## 🔗 Connecting to the PostgreSQL Database
base = psycopg2.connect(
    host="localhost",
    port="5432",
    database="youtubeapii",
    user="postgres",
    password="****"
)
conne = base.cursor()

e_gin = create_engine("postgresql://postgres:****@localhost:5432/youtubeapii")

## 📂 Video Categories (Category IDs)
('1', 'Film & Animation'),
('2', 'Autos & Vehicles'),
('10', 'Music'),
('17', 'Sports'),
('20', 'Gaming'),
('24', 'Entertainment'),
('25', 'News & Politics'),
('28', 'Science & Technology')
## 🌍  Countries
'TR': Turkey

'US': United States

'GB': United Kingdom

'IN': India

'DE': Germany


## 🧾 Save to Excel

dataf.to_excel("youtube_data.xlsx", index=True, engine='openpyxl')
## 🗃️ Save to PostgreSQL Database

dataf.to_sql("youtubeapii", e_gin, if_exists="replace", index=False)


