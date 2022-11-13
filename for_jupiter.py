from webdriver_manager.chrome import ChromeDriverManager
from collections.abc import MutableMapping
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import datetime
import requests
import random
import json
import time
import ast


########################################################################

def driver_get_200(driver, url):
    time_sleep = 0
    while True:
        time.sleep(time_sleep)
        while True:
            try:
                driver.get(url)
                break
            except:
                driver.switch_to.window(driver.window_handles[-1])

        time.sleep((random.randint(10, 40)) / 10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        if 'Непредвиденная ошибка' in soup.text:
            time_sleep += (random.randint(300, 800)) / 10
            print(f'Непредвиденная ошибка, поспим-ка {time_sleep} сек')
            time.sleep(time_sleep)
        else:
            break
    return driver


########################################################################

vpn_link = 'https://chrome.google.com/webstore/detail/vpn-freepro-free-unlimite/bibjcjfmgapbfoljiojpipaooddpkpai/related'

domen = 'https://lenta.com'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
driver = uc.Chrome(options=options)
driver = driver_get_200(driver, domen)


########################################################################

def add_link_to_json_db(links_to_check, driver):
    df = pd.read_feather('store.ft')
    diction = df.to_dict('records')
    for i, url in enumerate(links_to_check):
        print(f'{i + 1} из {len(links_to_check)}  {url}', end=' ')
        if df['link'].eq(url).any():
            print(f' - Уже скачан')
        else:
            time_sleep = 0
            try:
                driver = driver_get_200(driver, url)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                json_item = json.loads(
                    soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])
                diction.append({
                    'link': url,
                    'time': pd.Timestamp.now(),
                    'json_db': str(json_item),
                })
                pd.DataFrame.from_dict(diction).to_feather('store.ft')
                print(' - Добавлено', pd.Timestamp.now(), end=' ')
                post_time = random.randint(20, 80)/10
                print(f'Поспим {post_time} сек')
            except Exception as e:
                print(e)


with open('posuda.txt', "r") as f:
    links = ast.literal_eval(f.read())

with open('tovary-dlya-detejj.txt', "r") as f:
    links2 = ast.literal_eval(f.read())

add_link_to_json_db(links + links2, driver)

### Super IP 77.73.69.221