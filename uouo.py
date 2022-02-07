import requests
from bs4 import BeautifulSoup


class Spyder:
    class Company:
        LISTED = 1  # 上市
        OVER_THE_COUNTER = 2  # 上櫃

    _LINK_CLASS_PATTERN = 'Fw(b) Fz(20px) Fz(16px)--mobile Lh(23px) Lh(1.38)--mobile C($c-primary-text)! ' \
                          'C($c-active-text)!:h LineClamp(2,46px)!--mobile LineClamp(2,46px)!--sm1024 ' \
                          'mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) ' \
                          'LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled'

    _TITLE_CLASS_PATTERN = 'Mt(0) Mb(8px)'

    _AUTHOR_CLASS_PATTERN = 'C(#959595) Fz(13px) C($c-secondary-text)! D(ib) Mb(6px)'

    _ADS_CLASS_PATTERN = 'Fz(13px) C($c-secondary-text)! D(ib) Td(n) C(#959595) Mend(3px) Mb(6px)'

    _DOMAIN = 'https://tw.stock.yahoo.com'

    _DATE = 'caas-attr-time-style'

    @classmethod
    def get_classification(cls, company_type):
        response = requests.get(
            url=f'{cls._DOMAIN}/h/kimosel.php?tse={company_type}&cat=%A5b%BE%C9%C5%E9&form=menu&'
                f'form_id=stock_id&form_name=stock_name&domain=0')
        soup = BeautifulSoup(response.text, 'html.parser')
        classification_list = soup.find_all('a')
        data_list = list()
        for classification in classification_list:
            link = f'{cls._DOMAIN}{classification.get("href")}'
            if 'kimosel' not in link or f'tse={company_type}' not in link:
                continue
            data = {
                'name': classification.getText(),
                'link': link
            }
            data_list.append(data)
        return data_list

    @classmethod
    def get_code(cls):
        link = cls.get_classification(company_type=Spyder.Company.LISTED)
        code_list = list()
        for url in link:
            response = requests.get(url=url['link'])
            soup = BeautifulSoup(response.text, 'html.parser')
            stock = soup.find('a', {'class': 'none'})
            code = stock.getText().split(' ')[0]
            code_list.append(code[1:])
        return code_list

    @classmethod
    def get_stock_info(cls):
        data_list = cls.get_classification(company_type=1)
        id_ = list()
        name_ = list()
        code_list = cls.get_code()

        for data in data_list:
            name_.append(data['name'])

        for code in code_list:
            id_.append(code)

        return name_, id_

    @classmethod
    def get_article(cls):
        title_list = list()
        author_ = list()
        time_ = list()
        title_name = list()
        url = f'{cls._DOMAIN}/quote/1101.TW/news'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3', {'class': cls._TITLE_CLASS_PATTERN})
        author_item = soup.find_all('div', {'class': cls._AUTHOR_CLASS_PATTERN})
        for item in titles:
            items = item.select_one('a').get('href')
            name = item.getText()
            title_list.append(items)
            title_name.append(name)

        for author in author_item:
            items = author.getText()
            author_.append(items)

        for item in title_list:
            if cls._DOMAIN not in item:
                continue
            response = requests.get(url=f'{item}')
            soup = BeautifulSoup(response.text, 'html.parser')
            time = soup.find('div', {'class': cls._DATE})
            items = time.select_one('time').get('datetime')[:10]
            time_.append(items)

        return author_, time_, title_name

    @classmethod
    def display(cls, author_, title_name, time_, name_, id_):
        for x, y, z in zip(author_, time_, title_name):
            print(f'"author":{x}  "time":{y}  "title":{z}')

        for x, y in zip(name_, id_):
            print(f'"name":{x} "code":{y}')


if __name__ == '__main__':
    author_list, time_list, title_ = Spyder.get_article()
    id_list, name_list = Spyder.get_stock_info()
    Spyder.display(author_=author_list, time_=time_list, title_name=title_, name_=name_list, id_=id_list)
