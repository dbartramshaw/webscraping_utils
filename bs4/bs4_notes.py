#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python 2

""" Some notes on using bs4
    How to access different parts of soup
"""



from bs4 import BeautifulSoup
import requests

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

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
url='https://enterprise.microsoft.com/en-us/digital-transformation/'
r = requests.get(url, headers=headers, timeout=10)



####################
# bs4 notes
####################

# Run bs4
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'lxml')
for script in soup(["script", "style"]):
    script.extract()

org_text = soup.get_text()
text = org_text.replace("\n"," ")
text = ' '.join(text.split())



# Get soup from saved unicode HTML
soup = BeautifulSoup(test_html,"lxml")


# Find all links on a page
soup.find_all('a')
for link in soup.find_all('a'):
    print(link.get('href'))


# Find a certain class on a page
soup.findAll("div", { "class" : "c-article-template__info" })


# find certain tag and extract text
for hit in soup.findAll("div", { "class" : "c-article-template__info" }):
    print ' '.join(hit.text.split())


# Find heading
soup.find('h1')
soup.find('h1').text.strip()


#Remove script
for script in soup(["script", "style"]):
                script.extract()

#remove footer area
for script in soup.findAll("section", { "id" : "footerArea" }):
    script.extract()


# Show sections
for section in soup.findAll("section"):
    print(section.get('id'))

#Clean text
org_text = soup.get_text()
text = org_text.replace("\n"," ")
text = ' '.join(text.split())


# video link
# Store all youtube videos on page
videos_stored=[]
for i in range(0,len(data)):
    print i
    soup = BeautifulSoup(data.html[i], 'lxml')
    for script in soup.find_all('a'):
        search_links=[]
        if script.get('href')==None:
            print 'None'
            print script
        elif (script.get('href')).find('youtube') >0:
            print '______gottcha______'+(script.get('href'))
            search_links.append(script.get('href'))
            search_links.append(data.url[i])
            #print 'NO      '+(link.get('href'))
            videos_stored.append(search_links)

videos = pd.DataFrame(videos_stored,columns=['video','url'])
videos['video'].unique()
videos.groupby('video').size().sort_values()



####################
# Google Search
####################
# Links from google search - removing wierd hyperlink components
urls = ['https://www.google.co.uk/search?q=sore+on+gums&dcr=0&ei=MQhyWo-WM-ycgAacnIa4Bg&start=10&sa=N&biw=1680&bih=1669']

links=[]
for url in urls:
    page = requests.get(url)
    #print('Loaded page with: %s' % page)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.find_all('a')

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.find_all('a'):
        print(link.get('href'))

    import urlparse
    for a in soup.select('.r a'):
        print urlparse.parse_qs(urlparse.urlparse(a['href']).query)['q'][0]
        links.append(urlparse.parse_qs(urlparse.urlparse(a['href']).query)['q'][0])



####################
# webbrowser
####################
import webbrowser
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open(URL)

for i in range(0,10):
    webbrowser.get(chrome_path).open(pdfs.values[i])
