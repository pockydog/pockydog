import unittest
import requests


class TestStringMethods(unittest.TestCase):
    domain = 'https://royalcricket11-api.snoopyd.com'
    url = 'https://royalcricket11-dms-api.snoopyd.com'

    def test_login(self):
        url = f'{self.domain}/login/phone'
        payload = {
            'phone': '+886911486758',
            'password': '11111111'
        }
        headers = {
            'Version': '0.1'
        }
        response = requests.post(url=url, json=payload, headers=headers)
        info = response.json()
        token = info['data']['token']
        print(response.text)
        return token

