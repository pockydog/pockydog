import requests
import re
from bs4 import BeautifulSoup


class Test:
    _domain = 'http://www.vscinemas.com.tw/vsweb/film'
    _NOW = '/index.aspx'
    _READY = '/coming.aspx'

    @classmethod
    def get_url(cls):
        url_list = list()
        response = requests.get(url=f'{cls._domain}/coming.aspx' )
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_url = soup.find_all('a')
        for movie in movie_url:
            movie = movie.get('href')
            movie_ = str(movie)
            if 'https://www.vscinemas.com.tw/vsweb/' not in movie_ and 'detail.aspx?id=' in movie_:
                url_list.append(movie_)
        url_list = (set(url_list))
        return url_list

    @classmethod
    def get_info(cls):
        url_list = cls.get_url()
        temp = list()
        # type_list = list()
        # response = requests.get(url = 'http://www.vscinemas.com.tw/vsweb/film/detail.aspx?id=5686')
        for url in url_list:
            response = requests.get(url=f'{cls._domain}/{url}')
            soup = BeautifulSoup(response.text, 'html.parser')
            title_name = str(soup.find_all('h1')[1])
            name = title_name.replace('<h1>', '').replace('</h1>', '')
            title_time = str(soup.find_all('time'))
            time = title_time.replace('[<time>上映日期：', '').replace('</time>]', '')
            img_url = soup.find('div', {'class': 'movieMain'})
            img = img_url.find('img').get('src')
            img_url = img.replace('..', 'https://www.vscinemas.com.tw/vsweb')
            content = soup.find('div', {'class': 'bbsArticle'}).getText()
            content = content.strip()
            type = soup.find('div', {'class': 'markArea'})
            types = type.find_all('span')
            # type_list = '/'.join(i.get('class')for i in types)
            # b = list()
            # for i in types:
            #     b.append(i.get('class')[0])
            # type_list = '/'.join(b)
            result = {
                'name': name,
                'time': time,
                'content': content,
                'img_url': img_url
            }
            temp.append(result)
        return temp


if __name__ == '__main__':
    # Test.get_url()
    print(Test.get_info())




