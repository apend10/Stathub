import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

#Step1: create a variable called headers to tell the website that we are a browser and not a scraping tool
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

try:
    #Step 2: assigns the address of the page we need to scrape to a string
    page = "hi"

    #Step 3: uses the requests library to grab the code of a page and assign it to 'PageTree'
    pageTree = requests.get(page, headers=headers)
except:
    print("Improper URL Given!")