import requests
from bs4 import BeautifulSoup

class Test:

        _domain = 'https://www.harborfreight.com'

        @classmethod
        def get_url(cls):
            title_ = list()
            response = requests.get(url=cls._domain)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('span', {'role': 'presentation'}):
                title = link.getText().replace(' ', '-').replace('-&-', '-').lower()
                title_.append(title)
            return title_

        @classmethod
        def get_type_list(cls):
            titles = cls.get_url()
            title_name = list()
            for title in titles:
                response = requests.get(url=f'{cls._domain}/{title}.html')
                soup = BeautifulSoup(response.text, 'html.parser')
                types = soup.find_all('ul', {'class': 'subcategories__depSubList--1khMRx'})
                for type in types:
                    name = type.find('a').get('href')
                    title_name.append(f'{cls._domain}{name}')
            print(title_name)
            return title_name


        # @classmethod
        # def get_url(cls):
        #     title_name = cls.get_type_list()
        #     item_list = list()
            # for title in title_name:
            #     response = requests.get(url=f'{title}')
        #         soup = BeautifulSoup(response.text, 'html.parser')
        #         pages = soup.find('a', {'class': 'grid__itemTop--xogBBJ'})
        #         print(pages)



        # # @classmethod
        # # def get_po(cls):
        # #     item_list = cls.get_url()
        # #     print(item_list)
        #


if __name__ == '__main__':
#     # Test.get_url()
    Test.get_type_list()
    Test.get_url()
#     # Test.get_po()

