#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Save images from google search
    Old, inefficient but handy none the less for some quick images
    and for anyone learning bs4/python
"""

from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json


def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')


def pull_google_images(save_path = '/Users/bartramshawd/Pictures/google_search_pull/'):
        query = raw_input("query image")
        image_type=query
        query= query.split()
        query='+'.join(query)
        url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
        print url

        #add the directory for your image here
        DIR=save_path+query
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        soup = get_soup(url,header)

        ActualImages=[]
        for a in soup.find_all("div",{"class":"rg_meta"}):
            link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
            ActualImages.append((link,Type))
        print  "there are total" , len(ActualImages),"images"

        if not os.path.exists(DIR):
                    os.mkdir(DIR)

        ## Create a sub directory named of the search
        # DIR = os.path.join(DIR, query.split()[0])
        # if not os.path.exists(DIR):
        #            os.mkdir(DIR)


        ###print images
        print('Saving')
        for i , (img , Type) in enumerate( ActualImages):
            try:
                req = urllib2.Request(img, headers={'User-Agent' : header})
                raw_img = urllib2.urlopen(req).read()

                cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
                print cntr
                if len(Type)==0:
                    f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
                else :
                    f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')

                f.write(raw_img)
                f.close()
            except Exception as e:
                print "could not load : "+img
                #print e


pull_google_images()


##############
# PLAY CODE
##############
#
# query = raw_input("query image")# you can change the query for the image  here
# #query = 'badger'
#
# image_type="search"
# query= query.split()
# query='+'.join(query)
# url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
# print url
#
# #add the directory for your image here
# #DIR="Pictures"
# DIR='/Users/bartramshawd/Pictures/google_search_pull/'+query
# header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# soup = get_soup(url,header)
#
#
#
# ActualImages=[]# contains the link for Large original images, type of  image
# for a in soup.find_all("div",{"class":"rg_meta"}):
#     link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
#     ActualImages.append((link,Type))
# print  "there are total" , len(ActualImages),"images"
#
# if not os.path.exists(DIR):
#             os.mkdir(DIR)
#
# ## Create a sub directory named of the search
# # DIR = os.path.join(DIR, query.split()[0])
# # if not os.path.exists(DIR):
# #            os.mkdir(DIR)
#
#
# ###print images
# for i , (img , Type) in enumerate( ActualImages):
#     try:
#         req = urllib2.Request(img, headers={'User-Agent' : header})
#         raw_img = urllib2.urlopen(req).read()
#
#         cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
#         print cntr
#         if len(Type)==0:
#             f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
#         else :
#             f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')
#
#         f.write(raw_img)
#         f.close()
#     except Exception as e:
#         print "could not load : "+img
#         #print e
