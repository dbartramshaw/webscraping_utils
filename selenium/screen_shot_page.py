#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 2

""" A couple of utils to take tailored screengrabs using selenium
"""


import pandas as pd
from selenium import webdriver
import datetime
import os

'''
## driver setup in terminal
$ cd $HOME/Downloads
$ wget http://chromedriver.storage.googleapis.com/2.22/chromedriver_mac32.zip
$ unzip chromedriver_mac32.zip
$ mkdir -p $HOME/bin
$ mv chromedriver $HOME/bin
$ echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
'''

csv_path='/Users/bartramshawd/Documents/DBS/python_code/webscrape_utils/selenium/'
urls = pd.read_csv(csv_path+'example_urls.csv')
urls.head()

def driver_screenshot(url_list, folder_name='screenshots'):
    import pandas as pd
    from selenium import webdriver
    print 'RUNNING ...'
    start = datetime.datetime.now()
    save_path = csv_path+folder_name
    if not os.path.exists(save_path):
            os.makedirs(save_path)

    ### Chrome
    #DRIVER = '/Users/bartramshawd/bin/chromedriver'
    #driver = webdriver.Chrome(DRIVER)

    ### Firefox
    driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
    #driver.execute_script("document.body.style.zoom='75%'")

    driver.set_window_size(1000, 2000)
    for i in range(0,len(url_list)):
        iter_start = datetime.datetime.now()
        driver.get(url_list[i])
        screenshot = driver.save_screenshot(save_path+'/'+str(i)+'.png')
        print str(i)+ '  saved in '+str(datetime.datetime.now()-iter_start)+' seconds'
    driver.quit()
    print 'COMPLETE: '+str(len(url_list))+' Screenshots saved in '+str(datetime.datetime.now()-start)+' seconds'
    print 'LOCATION: '+save_path

## Run it
driver_screenshot(urls.url[0:10], folder_name='driver_screenshot_examples')


def phantomJS_screenshot(url_list, folder_name='test_folder'):
    """
        Ghost driver runs in the back end
        You can render much longer pages than visable on the pages
        Typically you see no ads on a page either - unless you feed in cookies
    """
    import pandas as pd
    import PIL
    from PIL import Image
    from selenium import webdriver
    import StringIO
    print 'RUNNING ...'
    start = datetime.datetime.now()
    save_path = csv_path+folder_name
    if not os.path.exists(save_path):
            os.makedirs(save_path)
    driver = webdriver.PhantomJS()
    driver.set_window_size(2000, 8000)
    for i in range(0,len(url_list)):
        iter_start = datetime.datetime.now()
        driver.get(url_list[i])
        screen = driver.get_screenshot_as_png()
        #box = (0, 0, 1700, 2000)
        im = Image.open(StringIO.StringIO(screen))
        #region = im.crop(box)
        #region.save(save_path+'/phantom_screen_'+str(i)+'.png')
        im.save(save_path+'/phantom_screen_new4k_'+str(i)+'.png')
        #, optimize=True, quality=95)
        print str(i)+ '  saved in '+str(datetime.datetime.now()-iter_start)+' seconds'
    driver.quit()
    print 'COMPLETE: '+str(len(url_list))+' Screenshots saved in '+str(datetime.datetime.now()-start)+' seconds'
    print 'LOCATION: '+save_path


## Run it
phantomJS_screenshot(urls.url[0:10], folder_name='phantomJS_screenshot_examples')
