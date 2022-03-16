from bs4 import BeautifulSoup
import requests

response = requests.get('https://tw.stock.yahoo.com/quote/2330.TW/news')
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('h3', {'class': 'Mt(0) Mb(8px)'})
authors = soup.find_all('div', {'class': 'C(#959595) Fz(13px) C($c-secondary-text)! D(ib) Mb(6px)'})
link_list = list()
date_list = list()
title_list = list()
author_list = list()
for author in authors:
    author = author.getText()
    author_list.append(author)

for title in titles:
    domain = title.select_one('a').get('href')
    title_name = title.select_one('a').getText()
    link_list.append(domain)
    title_list.append(title_name)

for link in link_list:
    response = requests.get(f'{link}')
    soup = BeautifulSoup(response.text, 'html.parser')
    datas = soup.find_all('div', {'class': 'caas-attr-time-style'})
    for data in datas:
        time = data.select_one('time').get('datetime')
        date_list.append(time[:10])

list_combineds = list(zip(title_list, date_list, author_list))
for list_combined in list_combineds:
    print(list_combined)

responses = requests.get('https://tw.stock.yahoo.com/h/kimosel.php?tse=1&cat=%A5b%BE%C9%C5%E9&form=menu&form_id=stock_id&form_name=stock_name&domain=0')
soup = BeautifulSoup(responses.text, 'html.parser')
stock_name = soup.find_all('td', {'class': 'c3'})
link_list = list()
for link in soup.find_all('a'):
    domain = link.get('href')
    stock = f'https://tw.stock.yahoo.com{domain}'
    link_list = list()
    if 'kimosel' in stock:
        link_list.append(stock)
        if '' in link_list:
            link_list.remove('')
    for link in link_list:
        responses = requests.get(f'{link}')
        soup = BeautifulSoup(responses.text, 'html.parser')
        stock_id = soup.find_all('a', {'class': 'none'})
        for stock in stock_id:
            print(stock.getText())


responses = requests.get('https://tw.stock.yahoo.com/h/kimosel.php?tse=2&cat=%C2d%A5b%BE%C9&form=menu&form_id=stock_id&form_name=stock_name&domain=0')
soup = BeautifulSoup(responses.text, 'html.parser')
stock_name = soup.find_all('td', {'class': 'c3'})
link_list = list()
for link in soup.find_all('a'):
    domain = link.get('href')
    stock = f'https://tw.stock.yahoo.com{domain}'
    link_list = list()
    if 'kimosel' in stock:
        link_list.append(stock)
        if '' in link_list:
            link_list.remove('')
    for link in link_list:
        responses = requests.get(f'{link}')
        soup = BeautifulSoup(responses.text, 'html.parser')
        stock_id = soup.find_all('a', {'class': 'none'})
        for stock in stock_id:
            print(stock.getText())
