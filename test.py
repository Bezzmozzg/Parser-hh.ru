from bs4 import BeautifulSoup
import requests

url = 'https://perm.hh.ru/search/vacancy?'

payload = {'area': '72',
           'st': 'searchVacancy',
           'fromSearch': 'true',
           'text': 'Python'}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/84.0.4147.89"
                  "Safari/537.36"}

offers = []
whith_price = []
whithout_price = []

page = requests.get(url, params=payload, headers=headers)

soup = BeautifulSoup(page.text, "html.parser")

offers = soup.findAll('div', class_='vacancy-serp-item__row vacancy-serp-item__row_header')

for i in offers:
    if len((i.find('div', class_="vacancy-serp-item__sidebar").text)) > 5:
        whith_price.append(" ".join(i.text.split()))
    else: whithout_price.append(" ".join(i.text.split()))

print(whithout_price)
print(whith_price)
