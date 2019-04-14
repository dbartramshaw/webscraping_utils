from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


##########################
# Facebook Login Example
##########################
user='username_here'
pwd='password_here'

# Or pop up windows
user = input("What is your facebook username (email) ")
pwd = input("What is your Facebook Password? ")

login_page = "http://www.facebook.com"
driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
driver.get(login_page)
assert "Facebook" in driver.title
driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)


# Verify it's worked
wait = WebDriverWait( driver, 5 )
try:
    page_loaded = wait.until_not(
    lambda browser: driver.current_url == login_page)
    print("Successful Login")
except TimeoutException:
    self.fail( "Loading timeout expired" )
# driver.close()


##########################
# Selenium Data Extraction
##########################
driver.current_url
driver.title
driver.page_source

# Get all images
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

# Download the image
import urllib
urllib.request.urlretrieve(image.get_attribute('src'), "example_image.png")


# Download all the images
images = driver.find_elements_by_tag_name('img')
counter=0
for image in images:
    counter+=1
    urllib.request.urlretrieve(image.get_attribute('src'), "selenium/saved_images/example_image"+str(counter)+".png")



##########################
# urllib3 Example
##########################
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
http = urllib3.PoolManager()
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

# Define page
url = 'http://www.thefamouspeople.com/singers.php'
url='https://www.instagram.com/p/yXor77n3l_/'


# Get page
response = http.request('GET', url,headers=header)
soup = BeautifulSoup(response.data, 'lxml')

# Extract Text (Strip crap)
for script in soup(["script", "style"]):
    script.extract()
org_text = soup.get_text()
text = org_text.replace("\n"," ")
text = ' '.join(text.split())

# Find title
title = soup.find('h1').text

# Find all images
imgs = soup.findAll("img",{"alt":True, "src":True})
for img in imgs:
    print(img["src"])



#########################
# Images from Instagram
#########################
import requests
import json
import sys
import urllib
import webbrowser
#http://myword.jeffreykishner.com/users/kishner/essays/030.html

url = 'https://www.instagram.com/whatchalookin_nat/'
data = requests.request('GET','http://api.instagram.com/publicapi/oembed/?url=' + url)
if data.status_code == 200:
    embed = json.loads(data.text)
    text_title = embed['title']
    img = embed['thumbnail_url']
    embed['html']
    print(img)
    img2 = urllib.parse.quote(img, '')
    print(img2)


def insta_pull(url):
    data = requests.request('GET','http://api.instagram.com/publicapi/oembed/?url=' + url)
    if data.status_code == 200:
        embed = json.loads(data.text)
        text_title = embed['title']
        img = embed['thumbnail_url']
        return text_title,img
    else:
        return '',''

text_title,img = insta_pull('https://www.instagram.com/p/BurruYAgTKs/')
text_title

from PIL import Image
import requests
from io import BytesIO

response = requests.get(img)
img = Image.open(BytesIO(response.content))
img


#########################
# Open in webdriver
#########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# option = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument("--window-size=1720,3000")
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.set_window_position(1600+1750, 0)
driver.set_window_size(1720,3000)

url_list =  ['https://www.medicare.gov',
             'https://www.medicaremadeclear.com',
             'https://www.allwellmedicare.com/',
             'https://www.azcompletehealth.com/',
             'https://www.uhcmedicaresolutions.com/',
             'https://www.uhc.com/',
             'https://www.azahcccs.gov/',
             'https://www.cigna.com/',
             'https://www.anthem.com/',
             'http://www.uhcprovider.com',
             'https://www.humana.com',
             'https://www.aarp.org',
             'https://www.hioscar.com',
             'https://seniors.lovetoknow.com',
             'https://www.nextavenue.org',
             'https://www.seniorliving.org']


for i in url_list:
    print(i)
    # driver.get(i)

    #Opens new tab
    driver.execute_script("window.open('"+i+"');")
driver.quit()



driver = webdriver.Chrome()
driver.get('https://www.instagram.com/p/yXor77n3l_/')





#########################
# AutoScroll
#########################

#Scroll until cannot scroll anymore
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
