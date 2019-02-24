#!/usr/bin/env python
# coding: utf-8

# # NASA Mars News

# In[1]:


# Dependencies
import requests
import pandas as pd
import os
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup  as bs 
from urllib.request import urlopen
from lxml import html


# In[ ]:





# In[2]:


def soup_read(url):
    webpage=requests.get(url)
    soup=bs(webpage, 'html.parser')
    return soup


# In[3]:


url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(url)


# In[4]:


# soup = bs(html_string, 'html.parser')
#type(soup)
# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html')
# response.text


# In[ ]:


# Examine the results, then determine element that contains sought info - works - use chrome tools instead
# print(soup.prettify())


# In[ ]:


# results are returned as an iterable list
# sample code - - - -results = soup.find_all('li', class_="result-row")

results = soup.find_all('div', class_="slide")


# # Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# 
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

# In[ ]:


# Loop through returned results  - works 
for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        mars_title = result.find('div', class_="content_title").find("a").text #title.a.text
        # Identify and return price of listing
        mars_body = result.find('div', class_="rollover_description_inner").text
#         # Identify and return link to listing
#         mars_link = result.a['href']

        # Print results only if title, price, and link are available
        if (mars_title and mars_body): #  and mars_body
            print('-------------')
            print(mars_title)
            print(mars_body)
#             print(mars_link)
    except AttributeError as e:
        print(e)


# # JPL Mars Space Images - Featured Image

# In[ ]:


# executable_path = {'executable_path': 'chromedriver.exe'}
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[ ]:


mars_image = requests.get(url2)
image_button = browser.find_by_id("full_image")
image_button.click()
browser.is_element_present_by_text("more info", wait_time=1)
m_info = browser.find_link_by_partial_text("more info")
m_info.click()
html = browser.html
html2 = bs(html,"html.parser")
featured_image = html2.select_one(".lede a img").get("src")
featured_image_url = "https://www.jpl.nasa.gov" + featured_image
print(featured_image_url)


# In[ ]:


# for link in soupjpl.find_all('article'):
#         print(link.get('style'))


# In[ ]:


# resultsjpl = soupjpl.find_all('article', class_='carousel_item')# id="full_image")
# print(len(resultsjpl))
# print(resultsjpl)
                              


# # Mars Weather - Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
# # Example: 
# mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'

# In[ ]:


url3 = 'https://twitter.com/marswxreport/'
mars_weather = requests.get(url3, timeout=10)
soup = bs(mars_weather.text, 'html.parser')
# print(soup.prettify())    

mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()#.strip()
print(mars_weather)


# In[ ]:





# # Mars Facts

# In[5]:


url_mf = 'https://space-facts.com/mars/'
tables = pd.read_html(url_mf)
tables


# In[6]:


df = tables[0]
df.head()


# In[ ]:


#to_html


# # Mars Hemispheres

# In[ ]:


url_mhemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

response = requests.get(url_mhemi, timeout=10)
soup = bs(response.text, 'html.parser')

results = soup.find_all('div')#, class_="content_title")
print(len(results))



# print(len(results))
# print(results)


# In[ ]:


# soup_mfact = soup_read('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
# # soup_mfact.title.text
# DEF=soup_mfact.findAll('p')
# DEF
# #div class'item'


# In[ ]:


# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
r = requests.get('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars', timeout=10)
r.status_code

# r.headers['content-type']
# r.encoding
r.text
# r.json()


# In[ ]:


mars_dict=dict()
from pprint import pprint
mars_dict["Mars_title"] = mars_title
mars_dict["Mars_news_body"] = mars_body
mars_dict["Mars featured Image"] = featured_image_url
mars_dict["Mars Weather"] = mars_weather
pprint(mars_dict)


# In[ ]:





# In[ ]:


# Dictionary to be inserted into MongoDB
    post = {
        'Mars_title': title,
        'Mars_news_body': lede,
        'date': article_date,
        'time published': time
    }

    # Insert dictionary into MongoDB as a document
    collection.insert_one(post)


# In[ ]:




