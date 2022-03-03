import requests
from bs4 import BeautifulSoup


class Test:
        _domain = 'https://www.harborfreight.com'

        @classmethod
        def get_title(cls):
            title_ = list()
            response = requests.get(url=cls._domain)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('span', {'role': 'presentation'}):
                title = link.getText().replace(' ', '-').replace('-&-', '-').lower()
                title_.append(title)
            return title_

        @classmethod
        def get_type_list(cls):
            titles = cls.get_title()
            title_name = list()
            for title in titles[:10]:
                response = requests.get(url=f'{cls._domain}/{title}.html')
                soup = BeautifulSoup(response.text, 'html.parser')
                types = soup.find_all('ul', {'class': 'subcategories__depSubList--1khMRx'})
                for type_ in types[:10]:
                    name = type_.find('a').get('href')
                    title_name.append(f'{cls._domain}{name}')
            return title_name

        @classmethod
        def get_url(cls):
            title_name = cls.get_type_list()
            url_list = list()
            for title in title_name[:10]:
                response = requests.get(url=f'{title}')
                soup = BeautifulSoup(response.text, 'html.parser')
                pages = soup.find_all('a', {'class': 'grid__itemTop--xogBBJ'})
                for page in pages[:10]:
                    name = page.get('href')
                    url_list.append(name)
            return url_list

        @classmethod
        def get_end(cls):
            url_list = cls.get_url()
            result = list()
            for url_ in url_list[:10]:
                response = requests.get(url=f'{cls._domain}{url_}')
                soup = BeautifulSoup(response.text, 'html.parser')
                item_title = url_.split('/')[3]
                item_name = soup.find('h1', {'class': 'product__title--Frjo0N'}).getText()
                item_price = soup.find('span', {'class': 'styled-price__styledPrice--Q537ya'}).getText()
                price = item_price[1:]
                price = float(price) / 100
                item_content = soup.find('div', {'class': 'overview__main--J35kh-'}).getText()
                img_url = soup.find('img').get('src')
                print(img_url)
                info = {
                    'name': item_name,
                    'title': item_title,
                    'price': price,
                    'content': item_content,
                    'img_url': img_url
                }
                result.append(info)
            return result


if __name__ == '__main__':
    print(Test.get_end())

