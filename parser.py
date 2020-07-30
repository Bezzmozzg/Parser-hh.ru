from bs4 import BeautifulSoup
import requests
import json

url = 'https://perm.hh.ru/search/vacancy?'

payload = {'area': '72',
           'st': 'searchVacancy',
           'fromSearch': 'true',
           'text': 'Java'}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/84.0.4147.89"
                  "Safari/537.36"}

result = []
name, worker_url, company_url, price, description = '','','','',''

page = requests.get(url, params=payload, headers=headers)

soup = BeautifulSoup(page.text, "html.parser")

for i in soup.findAll('div', class_='vacancy-serp-item'):
    name = "Name: " + i.find('a', class_="bloko-link HH-LinkModifier").text
    worker_url = 'Url: ' + i.find('a', class_="bloko-link HH-LinkModifier").get('href')
    company_url = 'Company_url: https://perm.hh.ru' + i.find('a', class_="bloko-link bloko-link_secondary").get('href')
    price = 'Price: ' + i.find('div', class_='vacancy-serp-item__sidebar').text
    if price == 'Price: ': price = 'Price: None'
    description = 'Description: ' + i.find('div', class_='g-user-content').text
    result.append([name, worker_url, company_url, price, description])

with open('result.json', 'w') as f:
    json.dump([result], f, ensure_ascii=False, indent=1)
