import pandas as pd
import ast
import random
import time
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import undetected_chromedriver as uc

domen = 'https://lenta.com'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
driver = uc.Chrome(options=options)
driver.get(domen)


def add_link_to_json_db(links_to_check):
    df = pd.read_feather('store.ft')
    diction = df.to_dict()
    for i, url in enumerate(links_to_check):
        print(f'{i + 1} из {len(links_to_check)}  {url}', end='')
        if url in diction['link']:
            print(f' - Уже скачан')
        else:
            try:
                time_sleep = random.randint(20, 80)
                while True:
                    time.sleep(random.randint(3, 6))
                    driver.get(url)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    if 'Непредвиденная ошибка' in soup.text:
                        print(f'Непредвиденная ошибка, поспим-ка {time_sleep} сек')
                        time_sleep += random.randint(30, 80)

                    else:
                        json_item = json.loads(
                            soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])

                        diction['link'].append(url)
                        diction['time'].append(pd.Timestamp.now())
                        diction['json_db'].append(json_item)
                        pd.DataFrame.from_dict(diction).to_feather('store.ft')

            except Exception as e:
                print(e)

def initialize_db():
    # with open('posuda.txt', "r") as f:
    #     links = ast.literal_eval(f.read())
    df = pd.DataFrame({
        'link': [''],
        'time': [pd.Timestamp.now()],
        'json_db': [''],
    })

    df.to_hdf('store.h5', key='df', mode='w')
    df.to_feather('store.ft')
    df.to_pickle('store.pkl')


# initialize_db()


def driver_get_200(driver, url):
    time_sleep = 0
    while True:
        time.sleep(time_sleep)
        driver.get(url)
        time.sleep((random.randint(10, 40))/10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        if 'Непредвиденная ошибка' in soup.text:
            time_sleep += (random.randint(300, 800))/10
            print(f'Непредвиденная ошибка, поспим-ка {time_sleep} сек')
            time.sleep(time_sleep)
        else:
            break
    return driver


#### 2 ####
vpn_link = 'https://chrome.google.com/webstore/detail/vpn-freepro-free-unlimite/bibjcjfmgapbfoljiojpipaooddpkpai/related'

domen = 'https://lenta.com'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
driver = uc.Chrome(options=options)
driver = driver_get_200(driver, domen)


# ast.literal_eval(pd.read_feather('store.ft').json_db[30])['adultWarning']
pd.read_feather('store.ft')


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
                print(' - Успешно добавлено', pd.Timestamp.now(), end=' ')
                post_time = time.sleep((random.randint(20, 80))/10)
                print(f'Поспим {post_time} сек')
            except Exception as e:
                print(e)


with open('posuda.txt', "r") as f:
    links = ast.literal_eval(f.read())

with open('tovary-dlya-detejj.txt', "r") as f:
    links2 = ast.literal_eval(f.read())

add_link_to_json_db(links + links2, driver)