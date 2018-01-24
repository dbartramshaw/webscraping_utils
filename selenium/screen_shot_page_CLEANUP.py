import pandas as pd
from selenium import webdriver
import datetime
import os
'''
$ cd $HOME/Downloads
$ wget http://chromedriver.storage.googleapis.com/2.22/chromedriver_mac32.zip
$ unzip chromedriver_mac32.zip
$ mkdir -p $HOME/bin
$ mv chromedriver $HOME/bin
$ echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
'''

#csv_path = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/'
csv_path = '/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/'
test_urls = pd.read_csv(csv_path+'ds_urls.csv')


def chrome_screenshot(url_list, folder_name='polyvore'):
    import pandas as pd
    from selenium import webdriver
    print 'RUNNING ...'
    start = datetime.datetime.now()
    save_path = csv_path+folder_name
    if not os.path.exists(save_path):
            os.makedirs(save_path)

    DRIVER = '/Users/bartramshawd/bin/chromedriver'
    driver = webdriver.Chrome(DRIVER)
    #driver.execute_script("document.body.style.zoom='75%'")
    driver.set_window_size(1700, 2000)
    #for i in range(0,len(url_list)):
    for i in range(0,4):
        iter_start = datetime.datetime.now()
        driver.get(url_list[i])
        screenshot = driver.save_screenshot(save_path+'/'+str(i)+'.png')
        print str(i)+ '  saved in '+str(datetime.datetime.now()-iter_start)+' seconds'
    driver.quit()
    print 'COMPLETE: '+str(len(url_list))+' Screenshots saved in '+str(datetime.datetime.now()-start)+' seconds'
    print 'LOCATION: '+save_path

i=1
i='https://leonella081104.polyvore.com/?filter=items'
url_list = ['https://michaelatodd333.polyvore.com/?filter=items','https://sasooza.polyvore.com/?filter=items','https://leonella081104.polyvore.com/?filter=items']

chrome_screenshot(URL, folder_name='test_folder')

chrome_screenshot(test_urls, folder_name='test_folder')



def phantomJS_screenshot(url_list, folder_name='test_folder'):
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
    #DRIVER = '/Users/bartramshawd/bin/chromedriver'
    #driver = webdriver.Chrome(DRIVER)
    #driver.execute_script("document.body.style.zoom='75%'")
    #for i in range(0,len(url_list)):
    for i in range(0,4):
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



phantomJS_screenshot(test_urls.url, folder_name='test_folder')







from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(700,500)
driver.get('http://tech.firstpost.com/news-analysis/aws-signs-java-father-james-gosling-377776.html')
driver.save_screenshot("/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot2.png")
driver.get('http://blog.yhat.com/posts/image-classification-in-Python.html')
driver.save_screenshot("/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot4.png")


driver.get('http://london.bigdataweek.com/?utm_source=sponsored-ad&utm_medium=LinkedIn&utm_campaign=EarlyBirdJune&utm_term=%233&utm_content=%233')
screen = driver.get_screenshot_as_png()

# Crop it back to the window size (it may be taller)
box = (10, 10, 1500, 1200)
im = Image.open(StringIO.StringIO(screen))
region = im.crop(box)
region.save('/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot00.png', optimize=True, quality=95)

im.save('/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot001.png', optimize=True, quality=95)

driver.quit()











sol_arc_urls = pd.read_csv(csv_path+'sol_arc_urls.csv')


''' Save a screenshot from spotify.com in current directory. '''
DRIVER = '/Users/bartramshawd/bin/chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.execute_script("document.body.style.zoom='75%'")
#driver.get('https://www.spotify.com')
driver.get('http://tech.firstpost.com/news-analysis/aws-signs-java-father-james-gosling-377776.html')
screenshot = driver.save_screenshot('/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot2.png')
driver.quit()

csv_path = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/'

###################
# DATA SCIENTISTS
####################
ds_path = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/screenshots/ds/'
if not os.path.exists(path):
        os.makedirs(path)

start = datetime.datetime.now()
driver = webdriver.Chrome(DRIVER)
driver.execute_script("document.body.style.zoom='75%'")
#for i in ds_urls.url
for i in range(0,len(ds_urls.url)):
    driver.get(ds_urls.url[i])
    screenshot = driver.save_screenshot(path+str(i)+'.png')
driver.quit()
print '__ Full Run complete __ in '+str(datetime.datetime.now()-start)+' seconds'
# ds = __ Full Run complete __ in 0:19:21.985480 seconds

ds_path = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/screenshots/ds/'
ds_files = list()
for i in range(0,len(ds_urls.url)):
    #ds_files.append(s_apath+str(i)+'.png')
    ds_files.append('<img src="'+s_apath+str(i)+'.png"/>')


# Required format
'<img src="image01.png"/>'

import pandas as pd
from IPython.display import Image, HTML
pd.set_option('display.max_colwidth', -1)

df = pd.DataFrame(ds_files, columns = ['Image'])
HTML(df.to_html(escape=False))





######################
# SOLUTIONS ARCHITECT
#######################
s_apath = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/screenshots/solutions_architect/'
if not os.path.exists(path):
        os.makedirs(path)

start = datetime.datetime.now()
driver = webdriver.Chrome(DRIVER)
driver.execute_script("document.body.style.zoom='75%'")
#for i in ds_urls.url
for i in range(0,len(sol_arc_urls.url)):
    driver.get(sol_arc_urls.url[i])
    screenshot = driver.save_screenshot(path+str(i)+'.png')
driver.quit()
print '__ Full Run complete __ in '+str(datetime.datetime.now()-start)+' seconds'
# ds = __ Full Run complete __ in 0:19:21.985480 seconds


s_apath = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/screenshots/solutions_architect/'
s_a_files = list()
for i in range(0,len(sol_arc_urls.url)):
    s_a_files.append(s_apath+str(i)+'.png')

import pandas as pd
from IPython.display import Image, HTML

df = pd.DataFrame(s_a_files, columns = ['Image'])
HTML(df.to_html(escape=False))




######################
# FEMALE CEO
#######################
ceo_female_urls = pd.read_csv(csv_path+'ceo_female_urls.csv')
ceo_path = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/screenshots/female_ceo/'
if not os.path.exists(ceo_path):
        os.makedirs(ceo_path)


driver = webdriver.Chrome(DRIVER)
driver.execute_script("document.body.style.zoom='75%'")
#for i in ds_urls.url
start = datetime.datetime.now()
for i in range(0,len(ceo_female_urls.url)):
    driver.get(ceo_female_urls.url[i])
    screenshot = driver.save_screenshot(ceo_path+'ceo_female_urls__'+str(i)+'.png')
driver.quit()
print '__ Full Run complete __ in '+str(datetime.datetime.now()-start)+' seconds'
# ds = __ Full Run complete __ in 0:19:21.985480 seconds


s_apath = '/Users/bartramshawd/Documents/MICROSOFT/pylon_output/azure/screenshots/solutions_architect/'
s_a_files = list()
for i in range(0,len(sol_arc_urls.url)):
    s_a_files.append(s_apath+str(i)+'.png')

import pandas as pd
from IPython.display import Image, HTML

df = pd.DataFrame(s_a_files, columns = ['Image'])
HTML(df.to_html(escape=False))



# Screen shot of entire page
import StringIO
from PIL import Image
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(700,500)
driver.get('http://tech.firstpost.com/news-analysis/aws-signs-java-father-james-gosling-377776.html')
driver.save_screenshot("/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot2.png")
driver.get('http://blog.yhat.com/posts/image-classification-in-Python.html')
driver.save_screenshot("/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot4.png")


driver.get('http://london.bigdataweek.com/?utm_source=sponsored-ad&utm_medium=LinkedIn&utm_campaign=EarlyBirdJune&utm_term=%233&utm_content=%233')
screen = driver.get_screenshot_as_png()

# Crop it back to the window size (it may be taller)
box = (10, 10, 1500, 1200)
im = Image.open(StringIO.StringIO(screen))
region = im.crop(box)
region.save('/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot00.png', optimize=True, quality=95)

im.save('/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot001.png', optimize=True, quality=95)

driver.quit()

driver = webdriver.Firefox()
print (driver.current_url)


#-- include('examples/showgrabbox.py')--#
import pyscreenshot as ImageGrab
if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
#-#


from selenium import webdriver
''' Save a screenshot from spotify.com in current directory. '''
DRIVER = '/Users/bartramshawd/bin/chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.execute_script("document.body.style.zoom='75%'")
#driver.get('https://www.spotify.com')
driver.set_window_size(1700, 2000)
driver.get('http://blog.yhat.com/posts/image-classification-in-Python.html')
screenshot = driver.save_screenshot('/Users/bartramshawd/Documents/CONTENT_OP/content_optimisation_beta/screenshots/my_screenshot9.png')
