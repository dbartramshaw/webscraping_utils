#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Find sitemap urls from sitemap

    ---------------------
    Added Capabilities
    ---------------------
        Can Handle nested sitemaps
        Can generate a list of pages that contain list of terms in url

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
def extract_intial_links(path, type='url'):
    '''
        Open an XML sitemap and find content wrapped in loc tags.

        -----------------------
        Type = ['url','file']
        -----------------------

        RETURNS:
                All sitemap urls
                All Non sitemap urls
    '''
    if type=='url':
        page_name = path
        page = requests.get(path)
        #print('Loaded page with: %s' % page)
        soup = BeautifulSoup(page.content, 'html.parser')

    elif type=='file':
        infile = open(path,"r")
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
        page_name = 'file'
        # print('file loaded')
    else:
        print("Type = ['url','file']")

    # gather links
    links = [element.text for element in soup.findAll('loc')]

    # define sitemaps (Non explicit)
    sitemap_urls1 = [element.loc.text for element in soup.findAll('sitemap')]

    # define sitemaps (explicit xml)
    sitemap_urls2 = [x for x in links if x[-4:]=='.xml']

    sitemap_urls = list(set(sitemap_urls1+sitemap_urls2))
    nonsitemap_urls = list(set(links)-set(sitemap_urls))

    return sitemap_urls, nonsitemap_urls



def find_all_pages(sitemap_url, type='url'):
    """
        Allows for single or nested sitemap.xmls
    """
    global sitemap_urls, url, sitemap_urls_master,sitemap_dict,error_sitemaps
    # Find other sitemaps or pages
    sitemap_urls, page_urls  = extract_intial_links(sitemap_url,type=type)
    page_urls_master=page_urls
    sitemap_urls_master=sitemap_urls
    sitemap_dict={}
    error_sitemaps =[]

    # Extract all nested sitemaps
    while len(sitemap_urls)>0:
        print(sitemap_urls)
        for url in sitemap_urls:
            try:
                print('PROCESSING:',url)
                # print('SITEMAP URLS',sitemap_urls)
                sitemap_urls.remove(str(url))
                sitemap_urls_new, page_urls = extract_intial_links(url,type=type)
                #update current sitemaps to run through -  remove those that have already ran!
                sitemap_urls = list(set(sitemap_urls_new+sitemap_urls)-set(sitemap_urls_master))
                #update history of sitemaps
                sitemap_urls_master+=sitemap_urls_new
                print(sitemap_urls_new)
                #append to full page list
                page_urls_master = page_urls_master+page_urls
                print(len(page_urls),'pages')
                #store in page level dict
                sitemap_dict[url]=page_urls
            except:
                #sitemap_urls.remove(str(url))
                error_sitemaps.append(url)
                print('!!!! ERROR !!!! :',url)

    # append original sitemap
    sitemap_urls_master+=[sitemap_url]

    print('### SITEMAP EXTRACTION COMPLETE ###')
    print("TOTAL URLS",len(page_urls_master))
    print("TOTAL UNIQUE", len(list(set(page_urls_master))))
    return page_urls_master,sitemap_urls_master,sitemap_dict


####################
# Sitemap fetcher
####################
def sitemap_url_fetch(url,
                      page_name,
                      search_terms = ['/iot','iot/','internet-of-things'],
                      search_name = 'iot',
                      save_path = '/Users/dshaw/Documents/DBS/python_code/webscrape_utils/'):
    """
        This runs a sitemap through extraction as well as extract all pages that include certain terms in the url

    """
    print(url,page_name,search_terms, search_name, save_path)
    all_links, all_sitemaps, sitemap_dict = find_all_pages(url)
    all_links=list(set(all_links))
    print('LOADED: all urls',len(all_links))

    df = pd.DataFrame(all_links,columns=['url'])
    df['rootpage']= page_name
    save_name = page_name.replace('https://','').replace('.','_').replace('/','')
    df.to_csv(save_path+'all_links_'+save_name+'.csv',encoding='utf-8')

    # search for iot
    import re
    words_re = re.compile("|".join(search_terms))
    search_url = [x for x in all_links if words_re.search(x)]
    print('LOADED: term urls', len(search_url))
    df_search = pd.DataFrame(search_url,columns=['url'])
    df_search['rootpage']=page_name
    df_search.to_csv(save_path+search_name+'_links_'+save_name+'.csv')
    print('***COMPLETE***')
    print(len(df),len(df_search))

    return df, df_search



####################
# Example Run
####################
df, df_search = sitemap_url_fetch(url ='https://www.3ds.com/sitemap/sitemap.xml',
                      page_name='https://www.3ds.com',
                      search_terms = ['/iot','iot/','internet-of-things'],
                      search_name = 'iot',
                      save_path = '/Users/dshaw/Documents/LIVE_BRIEFS/MSFT_seattle/loom_utils/data/')



sitemap_urls_new, page_urls = extract_intial_links('https://www.sce.com/sitemap.xml',type='url')
