from bs4 import BeautifulSoup, UnicodeDammit
import requests, json
import pandas as pd
import numpy as np
import datetime as dt

url = "http://feeds.feedburner.com/Kanji-a-dayLevel1"

jisho_link = "https://jisho.org/search/"

r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features='html.parser')

list_of_kanji = soup.find_all("item")

new_kanjis = []

for kanji in list_of_kanji:                                 

    try:

        title = kanji.find('title').text                     # Find Title, Description, and date of posting
        description = kanji.find('description').text
        date_text = kanji.find('pubdate').text

        desc = description.partition('<img ')               # Breaks description of useless ending text
        desc, _, _ = desc
        desc = desc.split('<br>')

        kanji_of_this_day = title

        on_reading_text = desc[0]                            # Pulls onyomi readings
        on_readings = on_reading_text[12:]
        
        kun_readings_text = desc[1]                          # Pulls kunyomi readings
        kun_readings = kun_readings_text[13:]

        meanings_text = desc[2]                              # Pulls meaning
        meanings = meanings_text[11:]

        date_posted =pd.to_datetime(date_text[:-15])         # Converts date posting to datetime to use in frame index later
        
        kanji_link = jisho_link + str(kanji_of_this_day) + "%20%23kanji"
        print(kanji_link)
        kanji_info = {'date':date_posted, 'kanji':kanji_of_this_day, 'on_read':on_readings, 'kun_read':kun_readings, 'meanings':meanings, 'jisho_link':kanji_link}

        new_kanjis.append(kanji_info)
    except:
        break

new_kanjis_df = pd.DataFrame(new_kanjis)
new_kanjis_df.set_index('date', inplace=True)

existing_kanji = pd.read_csv('C:\\Users\\mitch\\Desktop\\My Python\\kanji_list.csv')
existing_kanji['date'] = pd.to_datetime(existing_kanji.date)
existing_kanji.set_index('date', inplace=True)


brand_new_kanji = new_kanjis_df[new_kanjis_df.index > existing_kanji.index[0]]

completed_df = pd.concat([brand_new_kanji, existing_kanji], axis=0)
completed_df.to_csv('C:\\Users\\mitch\\Desktop\\My Python\\kanji_list.csv')