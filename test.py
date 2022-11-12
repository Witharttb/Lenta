import requests
import pprint
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
import json
import ast


def session_initial():
    s = requests.Session()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': 'qrator_jsr=1668231441.496.79cxuS1wC6djQP91-teg6k1fecbedrl7cfdlhibrlb45r5e3j-00; qrator_jsid=1668231441.496.79cxuS1wC6djQP91-ckjfpmrglki0g6pt9u26fj7krmcjehae; .ASPXANONYMOUS=xlPy7klTj5zIOBBcqDK9g0LiuO3Qpk4tbj0EEqtkPM53-LkJFc0-sxdsNeNj_Nfa-gCc885qKdlWtLTm6FeWZkxE9t1d8Ffxggihkj9c2RAcGm6YiGhq4F5rZIO1z9ksUvnevA2; ASP.NET_SessionId=knz1tp3hjesbo0h2mgvlwye3; cookiesession1=678B286DACDEGHIJKLMNOPQRSTUV86A5; qrator_ssid=1668231443.963.TJBzsE5WBjQmDEMa-3lddmgjir36nfskp3r212londsqvi1i6',
        'Host': 'lenta.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    s.get('https://lenta.com/', headers=headers)
    return s


def parse_header(filename):
    header = dict()
    with open(filename, 'r') as data:
        lines = data.readlines()
    for line in lines:
        if line.startswith(":"):
            a, b = line[1:].split(":", 1)
            a = f":{a}"
        else:
            a, b = line.split(":", 1)
        header[a.strip()] = b.strip()
    return header


def get_soup(url):
    sleep_time = (random.randint(30, 60))/10
    print(f'Поспим {sleep_time} секунд')
    time.sleep(sleep_time)

    while True:
        headers = parse_header('200.txt')
        pprint.pprint(headers)
        r = requests.get(url=url, headers=headers)
        if r.status_code == 200:
            break
        else:
            sleep_time += random.randint(3, 6)
        print(f'Статус код - {r.status_code} Поспим {sleep_time} секунд')
        time.sleep(sleep_time)

    soup = BeautifulSoup(r.content, 'lxml')
    print(soup)
    return soup


def get_dict_from_links(input_list, limit=5):
    # s = requests.Session()
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    # }
    # s.get('https://lenta.com/', headers=headers)
    nothing = 'missing'

    if type(input_list) == str:
        with open(input_list, "r") as f:
            links = ast.literal_eval(f.read())
    else:
        links = input_list

    all_in_one = []
    brend = []
    gacategory = []
    description = []
    cardPrice = []
    regularPrice = []
    sku = []
    link_small_img = []
    many = []
    stockValue = []
    storeAddress = []
    title = []
    subTitle = []
    img_urls = []
    link = []
    json_files = []

    for idx, url in enumerate(links):
        if idx == limit:
            print(f'Лимит {limit} достигнут, прерываю...')
            break
        print(f'{idx + 1} из {len(links)}  {url}')
        try:
            soup = get_soup(url)
            json_file = json.loads(
                soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])
            json_files.append(json_file)

            properties = json_file['attributesGroups'][0]['properties']

            try:
                all_in_one.append('\n'.join([item['key'] + ' : ' + item['value'] for item in properties]))
            except:
                all_in_one.append(nothing)
            try:
                brend.append(json_file['brand'])
            except:
                brend.append(nothing)
            try:
                gacategory.append(json_file['gaCategory'])
            except:
                gacategory.append(nothing)

            try:
                description.append(json_file['description'])
            except:
                description.append(nothing)

            try:
                cardPrice.append(json_file['cardPrice']['value'])
            except:
                cardPrice.append(nothing)

            try:
                regularPrice.append(json_file['regularPrice']['value'])
            except:
                regularPrice.append(nothing)

            try:
                sku.append(json_file['code'])
            except:
                sku.append(nothing)

            try:
                link_small_img.append(json_file['shareSkuMetaImageUrl'])
            except:
                link_small_img.append(nothing)

            try:
                many.append(json_file['stock'])
            except:
                many.append(nothing)

            try:
                stockValue.append(json_file['stockValue'])
            except:
                stockValue.append(nothing)

            try:
                storeAddress.append(json_file['storeAddress'])
            except:
                storeAddress.append(nothing)

            try:
                title.append(json_file['title'])
            except:
                title.append(nothing)

            try:
                subTitle.append(json_file['subTitle'])
            except:
                subTitle.append(nothing)

            try:
                img_urls.append(', '.join([item['full'] for item in json_file['imageUrls']]))
            except:
                img_urls.append(nothing)


        except Exception as e:
            print('Error', e)
            all_in_one.append(nothing)
            brend.append(nothing)
            gacategory.append(nothing)
            description.append(nothing)
            cardPrice.append(nothing)
            regularPrice.append(nothing)
            sku.append(nothing)
            link_small_img.append(nothing)
            many.append(nothing)
            stockValue.append(nothing)
            storeAddress.append(nothing)
            title.append(nothing)
            subTitle.append(nothing)
            img_urls.append(nothing)
        link.append(url)

    diction = {

        'Категория': gacategory,
        'Артикул': sku,
        'Наименование': title,
        'Подзаголовок': subTitle,
        'Изображение товара': link_small_img,
        'Ссылка на страницу': link,
        'Обычная цена': regularPrice,
        'Цена по акции': cardPrice,
        'Склад': storeAddress,
        'Кол-во ед': many,
        'Кол-во': stockValue,
        'Описание товара': description,
        'Бренд': brend,
        'Ссылки на фото': img_urls,
        'Характеристики': all_in_one,
    }
    return diction, json_files


# diction, json_files = get_dict_from_links('posuda.txt', 1)

# print(pd.DataFrame(diction))


url = 'https://lenta.com/product/594595-kitajj-594595/'
headers = parse_header('200.txt')
# pprint.pprint(headers)

response = requests.get(url, headers=headers)
response.encoding = 'ISO-8859-1'
print(response.encoding)
print(response.status_code)
print(response.content)
soup = BeautifulSoup(response.content, 'lxml')

print(soup.original_encoding)
print()
print(soup)



def get_dict_from_links(input_list, limit=5):
    nothing = 'missing'

    if type(input_list) == str:
        with open(input_list, "r") as f:
            links = ast.literal_eval(f.read())
        #     elif type(links) != list:
    #         break
    print(input_list)
    else:
    links = input_list


    all_in_one = []
    brend = []
    gacategory = []
    description = []
    cardPrice = []
    regularPrice = []
    sku = []
    link_small_img = []
    many = []
    stockValue = []
    storeAddress = []
    title = []
    subTitle = []
    img_urls = []
    link = []
    json_files = []

    for idx, url in enumerate(links):
        if idx == limit:
            print(f'Лимит {limit} достигнут, прерываю...')
            break
        print(f'{idx + 1} из {len(links)}  {url}')
        try:
            check_links = ast.literal_eval(f.read())[:5]

            #             url = 'https://lenta.com/product/594595-kitajj-594595/'
            headers = parse_header('200.txt')
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')

            soup = get_soup(url)
            json_file = json.loads(
                soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])
            json_files.append(json_file)

            properties = json_file['attributesGroups'][0]['properties']

            try:
                all_in_one.append('\n'.join([item['key'] + ' : ' + item['value'] for item in properties]))
            except:
                all_in_one.append(nothing)
            try:
                brend.append(json_file['brand'])
            except:
                brend.append(nothing)
            try:
                gacategory.append(json_file['gaCategory'])
            except:
                gacategory.append(nothing)

            try:
                description.append(json_file['description'])
            except:
                description.append(nothing)

            try:
                cardPrice.append(json_file['cardPrice']['value'])
            except:
                cardPrice.append(nothing)

            try:
                regularPrice.append(json_file['regularPrice']['value'])
            except:
                regularPrice.append(nothing)

            try:
                sku.append(json_file['code'])
            except:
                sku.append(nothing)

            try:
                link_small_img.append(json_file['shareSkuMetaImageUrl'])
            except:
                link_small_img.append(nothing)

            try:
                many.append(json_file['stock'])
            except:
                many.append(nothing)

            try:
                stockValue.append(json_file['stockValue'])
            except:
                stockValue.append(nothing)

            try:
                storeAddress.append(json_file['storeAddress'])
            except:
                storeAddress.append(nothing)

            try:
                title.append(json_file['title'])
            except:
                title.append(nothing)

            try:
                subTitle.append(json_file['subTitle'])
            except:
                subTitle.append(nothing)

            try:
                img_urls.append(', '.join([item['full'] for item in json_file['imageUrls']]))
            except:
                img_urls.append(nothing)


        except Exception as e:
            print('Error', e)
            all_in_one.append(nothing)
            brend.append(nothing)
            gacategory.append(nothing)
            description.append(nothing)
            cardPrice.append(nothing)
            regularPrice.append(nothing)
            sku.append(nothing)
            link_small_img.append(nothing)
            many.append(nothing)
            stockValue.append(nothing)
            storeAddress.append(nothing)
            title.append(nothing)
            subTitle.append(nothing)
            img_urls.append(nothing)
        link.append(url)

    diction = {

        'Категория': gacategory,
        'Артикул': sku,
        'Наименование': title,
        'Подзаголовок': subTitle,
        'Изображение товара': link_small_img,
        'Ссылка на страницу': link,
        'Обычная цена': regularPrice,
        'Цена по акции': cardPrice,
        'Склад': storeAddress,
        'Кол-во ед': many,
        'Кол-во': stockValue,
        'Описание товара': description,
        'Бренд': brend,
        'Ссылки на фото': img_urls,
        'Характеристики': all_in_one,
    }
    return diction, json_files






