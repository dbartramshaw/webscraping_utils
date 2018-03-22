#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python 2

""" Using multiprocessing to speed up bs4
"""

import requests
from bs4 import BeautifulSoup
from time import sleep
from multiprocessing import Pool
import pandas as pd
import pickle


def get_listing(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    html = None
    links = None
    try:
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            listing_section = soup.select('#offers_table table > tbody > tr > td > h3 > a')
            links = [link['href'].strip() for link in listing_section]
    except Exception as ex:
        print(str(ex))
    finally:
        return links



# parse a single item to get information
def parse(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    info = []
    title_text = '-'
    location_text = '-'
    price_text = '-'
    title_text = '-'
    images = '-'
    text = '-'

    try:
        r = requests.get(url, headers=headers, timeout=10)
        sleep(2)

        if r.status_code == 200:
            #print('Processing..' + url)
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            title = soup.find('h1')
            if title is not None:
                title_text = title.text.strip()

            location = soup.find('strong', {'class': 'c2b small'})
            if location is not None:
                location_text = location.text.strip()

            price = soup.select('div > .xxxx-large')
            if (price is not None) and (price!=[]):
                price_text = price[0].text.strip('Rs').replace(',', '').replace('\n', '')


            images = soup.select('#bigGallery > li > a')
            img = [image['href'].replace('\n', '').strip() for image in images]
            images = '^'.join(img)

            new_soup=soup
            for script in new_soup(["script", "style"]):
                script.extract()
            org_text = new_soup.get_text()
            text = org_text.replace("\n"," ")
            text = ' '.join(text.split())


            info.append(url)
            info.append(title_text)
            info.append(location_text)
            info.append(price_text)
            info.append(images)
            info.append(text)
            info.append(html)
    except Exception as ex:
        print(str(ex))
    finally:
        if len(info) > 0:
            return '|||'.join(info)
        else:
            return None


# Test 1
# parse(all_sites.page.values[0])


##############
# Example
##############
all_sites = pd.read_csv('msft_site_example.csv')

# Run pooled
ms_info = []
p = Pool(10)  # Pool tells how many at a time
ms_info = p.map(parse, all_sites.page.values[0:100])
p.terminate()
p.join()


# Save to df
df_ms_info_pre = pd.DataFrame(ms_info)
df_ms_info_pre = df_ms_info_pre.fillna('')
df_ms_info = pd.DataFrame([sub.split("|||") for sub in df_ms_info_pre[0].tolist()])
df_ms_info.columns=['url','title_text','location_text','price_text','images','text','html']
df_ms_info = df_ms_info.drop_duplicates().reset_index()
df_ms_info.tail()
# df_ms_info.to_csv("scrape_full.csv",encoding='utf-8',sep='|')
