#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 2

""" A couple of utils to take tailored screengrabs using selenium
"""

import pandas as pd
from selenium import webdriver
import datetime
import os
import base64


'''
## driver setup in terminal
$ cd $HOME/Downloads
$ wget http://chromedriver.storage.googleapis.com/2.22/chromedriver_mac32.zip
$ unzip chromedriver_mac32.zip
$ mkdir -p $HOME/bin
$ mv chromedriver $HOME/bin
$ echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile

## NOT WORKING
# your executable path is wherever you saved the gecko webdriver
# export PATH=$PATH:/Users/dshaw/Downloads/geckodriver.exe
# geckodriver = "/Users/dshaw/Downloads/geckodriver.exe"
# browser = webdriver.Firefox(executable_path=geckodriver)

## WORKING
#brew install geckodriver
browser = webdriver.Firefox()

'''

csv_path = '/Users/bartramshawd/Documents/DBS/python_code/webscrape_utils/selenium/'
urls = pd.read_csv(path)

import signal
import pandas as pd
import signal
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# url = 'https://www.purina.co.uk/cats/cat-breeds/cat-breed-library/japanese-bobtail-long-hair'
# url ='https://www.purina.co.uk/cat/gourmet/product-range/mon-petit/duo-fish-menu'
# driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
# driver.get(url)
# source_ = driver.page_source


# added timeout for page load (15secs)
def driver_screenshot_timeout(url_list, folder_name='screenshots'):
    import pandas as pd
    import signal
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    print 'RUNNING ...'
    start = datetime.datetime.now()
    save_path = csv_path+folder_name
    if not os.path.exists(save_path):
            os.makedirs(save_path)
    global errors

    ### Firefox
    driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
    #driver.execute_script("document.body.style.zoom='75%'")
    driver.set_window_size(1500, 2500)
    errors=[]
    for i in range(0,len(url_list)):
        try:
            iter_start = datetime.datetime.now()
            driver.set_page_load_timeout(15)
            driver.get(url_list[i])
            # screenshot = driver.save_screenshot(save_path+'/'+str(i)+'.png')
            screenshot = driver.save_screenshot(csv_path+'/'+base64.b64encode(url_list[i])+'.png')
            print str(i)+ '  saved in '+str(datetime.datetime.now()-iter_start)+' seconds'

        except TimeoutException as ex:
            errors.append(url_list[i])
            print(i, "Exception has been thrown. " + str(ex))
        except:
            print(i, "other Exception has been thrown. " + str(ex))
            pass
    driver.quit()
    print 'COMPLETE: '+str(len(url_list))+' Screenshots saved in '+str(datetime.datetime.now()-start)+' seconds'
    print 'LOCATION: '+save_path


## Run it
driver_screenshot_timeout(urls.url[0:10], folder_name='driver_screenshots')
urls.head()


def driver_screenshot(url_list, folder_name='screenshots'):
    import pandas as pd
    from selenium import webdriver
    print 'RUNNING ...'
    start = datetime.datetime.now()
    save_path = csv_path+folder_name
    if not os.path.exists(save_path):
            os.makedirs(save_path)
    global errors
    ### Chrome
    #DRIVER = '/Users/bartramshawd/bin/chromedriver'
    #driver = webdriver.Chrome(DRIVER)

    ### Firefox
    driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
    #driver.execute_script("document.body.style.zoom='75%'")
    driver.set_window_size(1000, 2000)

    errors=[]
    for i in range(0,len(url_list)):
        signal.alarm(15)
        try:
            iter_start = datetime.datetime.now()
            driver.get(url_list[i])
            # screenshot = driver.save_screenshot(save_path+'/'+str(i)+'.png')
            screenshot = driver.save_screenshot(save_path+'/'+base64.b64encode(page_urls[i])+'.png')
            print str(i)+ '  saved in '+str(datetime.datetime.now()-iter_start)+' seconds'
        except TimeoutException:
            errors.append(i)
            print('TIMEOUT 15secs:',i)
            continue
    driver.quit()
    print 'COMPLETE: '+str(len(url_list))+' Screenshots saved in '+str(datetime.datetime.now()-start)+' seconds'
    print 'LOCATION: '+save_path



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
