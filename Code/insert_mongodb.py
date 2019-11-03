from pymongo import MongoClient
import json,os,sys


git_dir = sys.argv[1] #'/Users/qingyao/hacknlead/hacknlead2019/'

client = MongoClient()
db = client.goodexplorers
products_cl = db.products
countries_cl = db.countries
companies_cl = db.companies

with open(os.path.join(git_dir, 'Data','countries.json')) as f:
    countries = json.load(f)
with open(os.path.join(git_dir, 'Data','products.json')) as f:
    products = json.load(f)
with open(os.path.join(git_dir, 'Data','companies.json')) as f:
    companies = json.load(f)

for i,j in products.items():
    products_cl.insert_one({'product': i, 'countries': j})

for i, j in countries.items():
    countries_cl.insert_one({'country':i, 'factors':j})

for i, j in companies.items():
    companies_cl.insert_one({'company':i, 'countries':j})