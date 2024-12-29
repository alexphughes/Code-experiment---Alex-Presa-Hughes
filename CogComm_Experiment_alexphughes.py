import subprocess
import sys

subprocess.check_call([sys.executable, '-m','pip', 'install', 'requests', 'beautifulsoup4', 'selenium', 'pandas', 'textstat', 'textblob'])

from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
from psychopy import data
import re
import html

def clean_text(text):
    if text is None:
        return ""
    text = ''.join([char if ord(char) < 128 else ' ' for char in text])
    text = text.replace('â€™', "'")
    text = text.replace('â€œ', '"')
    text = text.replace('â€˜', "'")
    text = text.replace('â€“', '–')
    text = html.unescape(text)
    return text

def scrape_article(url): 
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("h1").get_text() if soup.find("h1") else None
    title = clean_text(title)
    return {"url": url, "title": title}

urls = [
"https://www.bbc.com/news/articles/cm2796pdm1lo",
"https://www.bbc.com/news/articles/c75lxypz7wqo",
"https://www.bbc.com/news/articles/cyv737vy376o",
"https://www.bbc.com/news/articles/c4g5vwxgyx3o",
"https://www.bbc.com/news/articles/cwy9xde4l21o",
"https://www.bbc.com/news/articles/c3vkqwe9wwdo",
"https://www.bbc.com/news/articles/ckgry8rpzn4o",
"https://www.bbc.com/news/articles/c62938gl6q1o",
"https://www.bbc.com/news/articles/ced99eznje9o",
"https://www.bbc.com/news/articles/cm2742rynqgo",
"https://www.bbc.com/news/articles/cd9nze488gxo",
"https://www.bbc.com/news/articles/ce89051rypdo",
"https://www.bbc.com/news/articles/c3vkvekpkzeo",
"https://www.bbc.com/news/articles/c04pvp5qr6no",
"https://www.bbc.com/news/articles/c4g5wdezxe7o",
"https://www.bbc.com/news/articles/ce3yqzx72zno",
"https://www.bbc.com/news/articles/cdxvdqg8214o",
"https://www.bbc.com/news/articles/c39l89j10e1o",
"https://www.bbc.com/news/articles/cx2l4dn802lo",
"https://www.bbc.com/news/articles/c62l5zdv7zko",
"https://www.bbc.com/news/articles/cly2818j7rko",
"https://www.bbc.com/news/articles/c0mzgv4x901o",
"https://www.bbc.com/news/articles/c79zxjj0j55o",
"https://www.bbc.com/news/articles/cx2nrg4deyjo"
]
articles = [scrape_article(url) for url in urls]

df = pd.DataFrame(articles)

df_articles["group"] = pd.cut(df_articles.index, bins=3, labels=["Group 1", "Group 2", "Group 3"])

df_articles["unique_ID"] = df_articles.index + 1

df["unique_ID"] = df.index + 1
print(df.head())

from textstat import textstat

df["number_of_words"] = df["title"].apply(lambda x: len(x.split()))
df["readability"] = df["title"].apply(lambda x: textstat.flesch_reading_ease(x))

from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

df["polarity"], df["subjectivity"] = zip(*df["title"].apply(get_sentiment))

date = data.getDateStr()
folder_path = "C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cognition and Communication/CogComm_Experiment"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
df_file = os.path.join(folder_path, f"News_Articles_Analysis_{date}.csv")
df.to_csv(df_file, index = False, encoding='utf-8')