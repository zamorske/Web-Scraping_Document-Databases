from bs4 import BeautifulSoup
from splinter import Browser

# executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
executable_path = {'executable_path':'C:/Users/zamor/Class_work/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

