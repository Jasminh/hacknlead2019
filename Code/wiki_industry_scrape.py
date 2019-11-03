import requests

import json

from datetime import datetime

from bs4 import BeautifulSoup
import time

def find_industry(company_str):
    list_industry = []
    company = company_str.replace(' ','_')
    response = requests.get('https://en.wikipedia.org/wiki/{}'.format(company))
    
    if response.status_code != 200:
        return(list_industry)
    soup = BeautifulSoup(response.content)
    infobox = soup.find_all('table', class_='infobox')
    if not len(infobox):
        return(list_industry)
    for i in infobox[0].find('tbody').find_all('tr'):
        if i.th:
            if i.th.get_text() == 'Industry':
                for j in i.td:
                    if j.string:
                        list_industry.append(j.string)
                if len(list_industry) == 0:
                    list_industry+= i.td.get_text('\t').split('\t')
    return(list_industry)

find_industry('Industrial and Commercial Bank of China')

company_industry = {}
all_industry = set()
with open('../Data/forbes2000.tsv') as f:
    for l in f:
        company = l.split('\t')[0]
        if company in company_industry:
            continue
        time.sleep(0.5)
        found = find_industry(company)
        company_industry[company] = found
        all_industry.update(found)

with open('../Data/company_industry.json', 'w') as f:
    json.dump(company_industry, fp = f)

with open('../Data/all_industry.txt', 'w') as f:
    print('\n'.join(all_industry), file = f)