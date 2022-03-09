import time
from selenium import webdriver
from random import randint
# from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    browser = webdriver.Chrome('./chromedriver')
    browser.get('https://fandream11.play-demo.com/sign/in')