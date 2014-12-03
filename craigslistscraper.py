# Written on July 7, 2014 by Andy Tu

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
import requests
import re

#BASE_PRICE is the minimum acceptable price to be included to the calculation of average price:
BASE_PRICE = 100

#The URL - search up a term and insert the url here to scrape for a specific item:
BASE_URL = "http://vancouver.en.craigslist.ca/moa/"

html = requests.get(BASE_URL)
soup = BeautifulSoup(html.text)

#variables used for finding average
total=0
count = 0
valuelist = []

#these loops calculate the average price
values = soup.find_all(class_="price")

for value in values:
    
    temp = (re.findall(r'\d+',str(value)))
    valuelist +=temp

for value in valuelist:
    if int(float(value)) >= BASE_PRICE:
        total +=int(float(value))
        count+=1

average = int( total/count)
#print(valuelist)
print('The average price of items sold is: $'+ str(average))
        
for link in soup.find_all(['a','span class="price"']):
    
    nums = link.get_text()
    num = re.findall(r'\d+',nums)
    numero=0
    
    try:
        numero = int(float(num[0]))
    except:
        pass
    
    if (numero >= BASE_PRICE) and (numero < average):
        print('$' + repr(numero))
        print('http://vancouver.en.craigslist.ca'+link.get('href'))

