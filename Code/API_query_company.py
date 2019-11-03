import requests
import json
import time
from datetime import datetime

username = 'HackAPI3'
password = 'xfzzzEOBEJrmWpi' # needs to be adjusted!
auth_url = "https://commerce.reuters.com/rmd/rest/xml/login?username=" + username + "&password=" + password + "&format=json"
response = requests.get(auth_url)
authToken = json.loads(response.text).get('authToken').get('authToken')

from bs4 import BeautifulSoup

def parse_html(string):
    soup = BeautifulSoup(string, 'html.parser')    

    texts = []
    for i in soup.find_all('p'):
        texts.append(i.get_text())
        
    return ' '.join(texts)

company_list = []
with open('../Data/forbes2000.tsv') as f:
    for l in f:
        company = l.split('\t')[0]
        company_list.append(company)
            
company_country = {}
for i in company_list:
    search_query = 'fulltext:({}) AND exploitation'.format(i)
    channelCat = 'TXT'\
    date_range = '2018.10.22-2019.11.02'
    language = 'en'
    url = 'http://rmb.reuters.com/rmd/rest/json/search?q=' + search_query + '&channelCategory=' + channelCat + '&mediaType=T&token=' + authToken + '&format=json' + '&dateRange=' + date_range + '&language=' + language
    response = requests.get(url)
    a = json.loads(response.text)
    
    if not 'results' in a:
        continue
    if not a['results']['numFound']:
        continue
    print(i, 'no. results', a['results']['numFound'])
    for r in a['results']['result']:
        print(r['headline'])
    
    countries = set()
    for res in a['results']['result']:
        if 'geography' in res:
            countries.update(res['geography'])

    company_country[i] = countries