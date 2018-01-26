# python 2

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import pickle
import sys
import json
from time import sleep as wait
import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
save_path = 'set-data/'


# WEBSCRAPE HEADER
import urllib2
urlAccesser = urllib2.build_opener()
urlAccesser.addheaders = [('User-Agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36")] #v. imp. to not get blocked by cloudflare

# EXAMPLE URL
URL= 'https://www.google.co.uk/search?biw=1680&bih=1713&tbm=isch&sa=1&ei=agFrWqsSxrpRq8eWsA8&q=clouds&oq=clouds&gs_l=psy-ab.3..0i67k1l3j0l2j0i67k1j0l4.1389.3278.0.3513.8.8.0.0.0.0.78.574.8.8.0....0...1c.1.64.psy-ab..0.8.572...0i7i30k1j0i10i24k1j0i24k1j0i13k1j0i8i7i30k1.0._HBnw275QEA'

# BS4 EXAMPLE
URL='http://all-that-is-interesting.com/david-bowie-photos'
html = urlAccesser.open(URL)
soup = BeautifulSoup(html, 'html.parser')
links_loop_test=[]
for link in soup.find_all('a'):
    links_loop_test.append(link.get('href'))
links_loop_test


#######################
## MANUAL SELENIUM
#######################

#Open browser
DRIVER = '/usr/local/bin/geckodriver'
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
#move to second screen
browser.set_window_position(6000, 0)
browser.get(URL)
print 'Start: '+strftime("%Y-%m-%d %H:%M:%S", gmtime())
print 'URL: '+URL
start = time.time()
time.sleep(1)

#Control Browser - no scrape yet
elem = browser.find_element_by_tag_name("body")
no_of_pagedowns = 40

#run until no more results only
# When we pull browser.any_function we will only see what is loaded on the screen
# So we need to scroll down
counter=0
while no_of_pagedowns and browser.find_elements_by_class_name("tsf-p")!='test': #ksb_kvc is googles class for "show more results", We could get it to click this button
    print(browser.find_elements_by_class_name("tsf-p").get_attribute('href'))
    print(browser.find_elements_by_class_name("tsf-p").get_attribute('id'))
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
    counter+=1



#images = browser.find_elements_by_tag_name('img')
#for image in images:
    #print(image.get_attribute('src'))

### pull all links ###
links_loop=[]
linksa = browser.find_elements_by_tag_name('a')
for lnk in linksa:
    links_loop.append(lnk.get_attribute('href'))
    #print(lnk.get_attribute('href'))
print 'links pulled'

### setid ###
set_id = [x for x in links_loop if x is not None and "set?id" in x]
# set_id_out = open(save_path+"set_id_ever.pickle","wb")
# pickle.dump(set_id, set_id_out)
# set_id_out.close()
print 'Set_id saved'

### comments ###
set_id_Comments = [x for x in links_loop if x is not None and '&id=' in x ]
#set_id_Comments_out = open(save_path+"set_id_comments_ever.pickle","wb")
#pickle.dump(set_id_Comments, set_id_Comments_out)
#set_id_Comments_out.close()
print 'set_id_Comments saved'

## End time
print 'End: '+strftime("%Y-%m-%d %H:%M:%S", gmtime())
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
print '__________________________________________________'
print str(counter)+' pagedowns used'
print str(len(set_id))+' set ids found'
browser.quit()




########################################
# STEP 1.1
# GET THE LINKS OF SETS UTIL
########################################
# set up selenium to scroll down to the bottom of each page
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.set_window_position(2000, 0)

def run_link_find(URL):
    # ! Uncomment to open new window every time
    # browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
    # browser.set_window_position(2000, 0)
    browser.get(URL)

    print 'Start: '+strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print 'URL: '+URL
    start = time.time()
    time.sleep(1)
    elem = browser.find_element_by_tag_name("body")
    no_of_pagedowns = 1000

    #run until no more results only
    counter=0
    while no_of_pagedowns and browser.find_elements_by_class_name("no_results")==[]:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1
        counter+=1

    ### pull all links ###
    links_loop=[]
    linksa = browser.find_elements_by_tag_name('a')
    for lnk in linksa:
        links_loop.append(lnk.get_attribute('href'))
    print 'links pulled'

    ### setid ###
    set_id = [x for x in links_loop if x is not None and "set?id" in x]
    print 'Set_id saved'

    ### comments ###
    set_id_Comments = [x for x in links_loop if x is not None and '&id=' in x ]
    print 'set_id_Comments saved'

    ## End time
    print 'End: '+strftime("%Y-%m-%d %H:%M:%S", gmtime())
    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
    print '__________________________________________________'
    print str(counter)+' pagedowns used'
    print str(len(set_id))+' set ids found'
    # ! Uncomment to open new window every time
    #browser.quit()
    return set_id,set_id_Comments



################################
# STEP 1.2 RUN
# LOOP FOR ALL COLOURS & CELEBS
# Links colected from dropdowns
################################
colours = [u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=white',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=grey',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=brown',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=beige',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=red',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=pink',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=orange',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=yellow',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=blue',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=light+blue',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=green',
           u'https://www.polyvore.com/cgi/search.sets?category=fashion&color=purple'
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Amanda+Seyfried',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Ariana+Grande',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Audrey+Hepburn',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Barbara+Palvin',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Beyonce+Knowles',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Blake+Lively',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Candice+Swanepoel',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Cara+Delevingne',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Demi+Lovato',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Doutzen+Kroes',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Emma+Watson',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Frida+Gustavsson',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Jennifer+Lawrence',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Justin+Bieber',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Kate+Moss',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Katy+Perry',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Kristen+Stewart',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Kristina+Bazan',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Lady+Gaga',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Lana+Del+Rey',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Lauren+Conrad',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Leighton+Meester',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Lily+Collins',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Lucy+Hale',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Luke+Hemmings',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Marilyn+Monroe',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Megan+Fox',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Miley+Cyrus',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Miranda+Kerr',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Niall+Horan',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Nina+Dobrev',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Olivia+Palermo',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Perrie+Edwards',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Rihanna',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Selena+Gomez',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Taylor+Momsen',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Taylor+Swift',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Vanessa+Hudgens',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Zayn+Malik',
         u'https://www.polyvore.com/cgi/search.sets?category=fashion&celebrity=Zendaya',
         u'https://www.polyvore.com/street-style-fashion/search.sets?category=fashion&query=street+style',
         u'https://www.polyvore.com/celebrity-fashion/search.sets?category=fashion&query=celebrity',
         u'https://www.polyvore.com/work-wear-fashion/search.sets?category=fashion&query=work+wear',
         u'https://www.polyvore.com/formal-fashion/search.sets?category=fashion&query=formal',
         u'https://www.polyvore.com/vacation-fashion/search.sets?category=fashion&query=vacation',
         u'https://www.polyvore.com/school-fashion/search.sets?category=fashion&query=school',
         u'https://www.polyvore.com/edgy-fashion/search.sets?category=fashion&query=edgy',
         u'https://www.polyvore.com/casual-fashion/search.sets?category=fashion&query=casual',
         u'https://www.polyvore.com/preppy-fashion/search.sets?category=fashion&query=preppy',
         u'https://www.polyvore.com/boho-fashion/search.sets?category=fashion&query=boho',
         u'https://www.polyvore.com/sporty-fashion/search.sets?category=fashion&query=sporty',
         u'https://www.polyvore.com/plus-size-fashion/search.sets?category=fashion&query=plus+size',
         ]


# ADDED FOR MORE VOLUME - Top words appearing in image meta from above
# This was gained by joing on the word clothing cat lkp
search_words = pd.read_csv(save_path+'top_search_words_non_clothes.csv')


################################
# Run around colours & celebs
################################
final_set_id=[]
final_set_id_Comments=[]
for URL in colours[1:3]:
    # ADDED FOR MORE VOLUME - Look at last 3month results & last day results
    for add in ['&date=day','&date=3m']:
        url = URL+add
        set_id_loop ,set_id_Comments_loop = run_link_find(url)
        #remove dupes
        set_id_loop=list(set(set_id_loop))
        set_id_Comments_loop=list(set(set_id_Comments_loop))
        print '--------------------------------------------------'
        print url
        print str(len(set_id_loop))+' set ids'
        print str(len(set_id_Comments_loop))+' set comment ids'
        final_set_id = final_set_id+set_id_loop
        final_set_id_Comments = final_set_id_Comments+set_id_Comments_loop
        #pickle.dump(final_set_id, open(save_path+"set_id_results.pickle", "wb" ))
        print 'SAVED final set id: '+ str(len(final_set_id))
        #pickle.dump(final_set_id_Comments, open(save_path+"set_id_comments_results.pickle", "wb" ))
        print 'SAVED final comments set id: '+ str(len(final_set_id_Comments))
        print '---------------------------------------------------'


################################
# Run around top search words
################################
for w_i in search_words.words:
    for add in ['https://www.polyvore.com/cgi/search.sets?.search_src=masthead_search&category=fashion&date=day&query=','https://www.polyvore.com/cgi/search.sets?.search_src=masthead_search&category=fashion&date=3m&query=']:
        url = add+w_i
        print(url)
        set_id_loop ,set_id_Comments_loop = run_link_find(url)
        #remove dupes
        set_id_loop=list(set(set_id_loop))
        set_id_Comments_loop=list(set(set_id_Comments_loop))
        print '--------------------------------------------------'
        print url
        print str(len(set_id_loop))+' set ids'
        print str(len(set_id_Comments_loop))+' set comment ids'
        final_set_id = final_set_id+set_id_loop
        final_set_id_Comments = final_set_id_Comments+set_id_Comments_loop

        pickle.dump(final_set_id, open(save_path+"set_id_results.pickle", "wb" ))
        print 'SAVED final set id: '+ str(len(final_set_id))
        pickle.dump(final_set_id_Comments, open(save_path+"set_id_comments_results.pickle", "wb" ))
        print 'SAVED final comments set id: '+ str(len(final_set_id_Comments))
        print '---------------------------------------------------'


# Reload data
# set_id_results = pickle.load( open(save_path+"set_id_results.pickle", "rb" ) )
# len(set(set_id_results))


######################################
# STEP 2.1: NOT NEEDED - USING SCRAPY
#
# SCRAPE THE URLS - GET THE IMG LINKS
######################################

# using beautiful soup
   # def scrape_imgs(url):
   #  scrape_dict={}
   #  html = urlAccesser.open(url)
   #  soup = BeautifulSoup(html, 'html.parser')
   #  html_str = str(soup)
   #
   #  #images = [img for img in soup.findAll('img')]
   #  images_tn = soup.findAll("img", { "class" : "img_size_m" })
   #  images_tn_list=[]
   #  for image in images_tn:
   #      img_dict_tn={}
   #      img_dict_tn['alt']= image['alt']
   #      img_dict_tn['src']= image['src']
   #      img_dict_tn['class']= image['class']
   #      img_dict_tn['title']= image['title']
   #      img_dict_tn['width']= image['width']
   #      images_tn_list.append(img_dict_tn)
   #
   #  like_class = soup.findAll("ul", { "class" : "actions new_actions clearfix" })
   #  likes = [span.get_text() for span in like_class][0]
   #  likes = int(likes.replace('u',''))
   #
   #  scrape_dict['imgs_tn']=images_tn_list
   #  scrape_dict['likes']=likes
   #  # print 'complete'
   #  return html_str, scrape_dict




################################
# STEP 2.2: NOT NEEDED - USING SCRAPY
#
# RUN SCRAPE, SCRAPE IMG URLS
################################
# dict_pull_bs4={}
# error_urls=[]
# counterB=0
# for i in set_id_results[:10]:
#     try:
#         html, dict_iter =scrape_imgs(i)
#         dict_pull_bs4[i]=dict_iter
#         #Save HTML File
#         with open(save_path+'html/'+binascii.hexlify(i)+'.html', "w") as file:
#             file.write(html)
#     except:
#         'error '+i
#         error_urls.append(i)
#
#     counterB+=1
#
#     print(counterB)
#
# #save errored URL (Will Have errored due to rejection - could repull)
# pd.DataFrame(error_urls).to_csv(save_path+'scrape_failed_urls.csv',index=None)
#


################################
# STEP 3.1
# SAVE IMGS TO FILE
################################

#Loop
# full_img_dict={}
# errors=[]
# counter=0
# del i
# for page in range(1,3000):
#     if counter < 10:
#         try:
#             page_dict = scrape_output[scrape_output.keys()[page]]['imgs_tn']
#             page_url = scrape_output.keys()[page]
#             img_lst = []
#             for i in page_dict:
#                 img_dict={}
#                 wt = random.uniform(1, 2)
#                 time.sleep(wt)
#
#                 #request and save
#                 url = i['src']
#                 r = requests.get(url, allow_redirects=True)
#                 name = 'group'+str(page)+'_'+url[url.find('tid/')+4:]
#                 open(save_path+'images/'+name, 'wb').write(r.content)
#
#                 #store in dict
#                 img_dict['group_number']=page
#                 img_dict['group_url']=page_url
#                 img_dict['title']=i['title']
#                 full_img_dict[name]=img_dict
#             #saftey save
#             with open(save_path+'image_dict_second.json', 'w') as fp:
#                 json.dump(full_img_dict, fp)
#             print(page)
#         except:
#             wt = random.uniform(5, 6)
#             time.sleep(wt)
#             print('ERROR',page)
#             errors.append(page)
#             counter+=1
