#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Find sitemap
"""

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import pickle
save_path='/sitemap_visualisation/'
from time import sleep as wait


######################
# From Site
######################
url='https://www.3ds.com/sitemap/sitemap.xml'
sitemap_apx=['/sitemap.xml','SiteMapAction.do','sitemap_index.xml','sitemap/sitemap-fr.xml']



def extract_links(path, type='url'):
    '''
        Open an XML sitemap and find content wrapped in loc tags.

        -----------------------
        Type = ['url','file']
        -----------------------
    '''
    if type=='url':
        page = requests.get(path)
        #print('Loaded page with: %s' % page)
        soup = BeautifulSoup(page.content, 'html.parser')
    elif type=='file':
        infile = open(path,"r")
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
    else:
        print("Type = ['url','file']")
    # print('Created %s object' % type(sitemap_index))
    links = [element.text for element in soup.findAll('loc')]
    return links


def find_all_pages(sitemap_url, type='url'):
    """
        Allows for single or nested sitemap.xmls
    """
    # Find other sitemaps or pages
    urls = extract_links(sitemap_url,type=type)
    sitemap_urls = [x for x in urls if x[-4:]=='.xml']
    page_urls = [x for x in urls if x[-4:]!='.xml']

    # Extract all nested sitemaps
    while len(sitemap_urls)>0:
        for url in sitemap_urls:
            print('PROCESSING:',url)
            sitemap_urls.remove(url)
            print(type)
            links = extract_links(url,type=type)
            sitemap_urls+= [x for x in links if x[-4:]=='.xml']
            page_urls += [x for x in links if x[-4:]!='.xml']
            print(len(page_urls),'pages')
    print('### SITEMAP EXTRACTION COMPLETE ###')
    return page_urls


# URL example
sitemap_url='https://www.3ds.com/sitemap/sitemap.xml'
all_links = find_all_pages(sitemap_url, type='url')

# file example
sitemap_file="/Users/bartramshawd/Documents/POSSIBLE/sitemaps_dentaquestinstitute/sitemap.xml"
all_links = find_all_pages(sitemap_file, type='file')
len(all_links) # 2107 pages



# # Run sitemap vis
# with open('sitemap_urls.dat', 'w') as f:
#     for url in all_links:
#         try:
#             f.write(url + '\n')
#         except:
#             pass
#
# python categorize_urls.py --depth 10
# python visualize_urls.py --depth 5 --title "Sitemap Overview" --size "10"


# file example
sitemap_file="/Users/bartramshawd/Documents/POSSIBLE/sitemaps_dentaquest/sitemap.xml"
all_links = find_all_pages(sitemap_file, type='file')
len(all_links) # 879 pages

# file example
sitemap_file="/Users/bartramshawd/Documents/POSSIBLE/sitemaps_dentaquestfoundation/sitemap.xml"
all_links = find_all_pages(sitemap_file, type='file')
len(all_links) # 83 pages
