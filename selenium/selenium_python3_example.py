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
