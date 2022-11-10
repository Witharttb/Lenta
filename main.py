# from multiprocessing import freeze_support
#
# from webdriver_manager.chrome import ChromeDriverManager
# import undetected_chromedriver as uc
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from pprint import pprint
# import pandas as pd
# import datetime
# import requests
# import json
# import time
# import ast
#
# domen = 'https://lenta.com'
# options = webdriver.ChromeOptions()
# options.add_argument('--blink-settings=imagesEnabled=false')
# # options.add_argument("--headless")
# driver = uc.Chrome(options=options)
# driver.get(domen)
# time.sleep(40)
#
# all_links = [
#     # 'https://lenta.com/catalog/bakaleya/',
#     #     'https://lenta.com/catalog/chajj-kofe-kakao/',
#     'https://lenta.com/catalog/zdorovoe-pitanie/',
#     #     'https://lenta.com/catalog/krasota-i-zdorove/',
#     #     'https://lenta.com/catalog/bytovaya-himiya/',
#     #     'https://lenta.com/catalog/sport-i-aktivnyjj-otdyh/',
#     #     'https://lenta.com/catalog/tovary-dlya-zhivotnyh/',
#     #     'https://lenta.com/catalog/lenta-zoomarket---professionalnyjj-uhod/',
#     #     'https://lenta.com/catalog/avtotovary/',
# ]
#
#
# def get_links_from_pages(all_links):
#     for i, url in enumerate(all_links):
#         print(f'{i + 1} из {len(all_links)}  {url}')
#         file_name_txt = f"{url.split('/')[-2]}.txt"
#         file_name_xlsx = f"{url.split('/')[-2]}.xlsx"
#
#         driver.get(url)
#         time.sleep(3)
#         driver.execute_script("window.scrollTo(0, 1000)")
#         time.sleep(1)
#
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'lxml')
#         time.sleep(4)
#         last_page_num = int(soup.find_all('li', class_='pagination__item')[-1].text)
#
#         links = []
#
#         last_page_num = 32
#
#         for page_num in range(1, last_page_num + 1):
#             url2 = f'{url}?page={page_num}'
#             print(url2)
#             try:
#                 driver.get(url2)
#                 time.sleep(2)
#                 driver.execute_script("window.scrollTo(0, 1000)")
#                 time.sleep(0.5)
#
#                 html = driver.page_source
#                 soup = BeautifulSoup(html, 'lxml')
#                 links += [domen + item.a['href'] for item in soup.find_all('div', class_='sku-card-small-container')]
#                 print(len(links))
#                 if len(links) == 0:
#                     break
#             except:
#                 pass
#
#         links = sorted(set(links))
#         print(f'Найдено {len(links)} товаров')
#
#     file_name_txt = f"{all_links[0].split('/')[-2]}.txt"
#     file_name_xlsx = f"{all_links[0].split('/')[-2]}.xlsx"
#     with open(file_name_txt, "w") as f:
#         try:
#             f.write(str(links))
#         except:
#             print(f"Не удалось записать файл {file_name_txt}")
#     return links
#
#
# def get_dict_from_links(input_list, limit=5):
#     nothing = 'missing'
#
#     if type(input_list) == str:
#         with open(input_list, "r") as f:
#             links = ast.literal_eval(f.read())
#         #     elif type(links) != list:
#     #         break
#
#     else:
#         links = input_list
#     all_in_one = []
#     brend = []
#     gacategory = []
#     description = []
#     cardPrice = []
#     regularPrice = []
#     sku = []
#     link_small_img = []
#     many = []
#     stockValue = []
#     storeAddress = []
#     title = []
#     subTitle = []
#     img_urls = []
#     link = []
#
#     for idx, url in enumerate(links):
#         if idx == limit:
#             print(f'Лимит {limit} достигнут, прерываю...')
#             break
#         print(f'{idx + 1} из {len(links)}  {url}')
#         try:
#             driver.get(url)
#             time.sleep(2)
#             html = driver.page_source
#             soup = BeautifulSoup(html, 'lxml')
#             json_file = json.loads(
#                 soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])
#             properties = json_file['attributesGroups'][0]['properties']
#
#             try:
#                 all_in_one.append('\n'.join([item['key'] + ' : ' + item['value'] for item in properties]))
#             except:
#                 all_in_one.append(nothing)
#             try:
#                 brend.append(json_file['brand'])
#             except:
#                 brend.append(nothing)
#             try:
#                 gacategory.append(json_file['gaCategory'])
#             except:
#                 gacategory.append(nothing)
#
#             try:
#                 description.append(json_file['description'])
#             except:
#                 description.append(nothing)
#
#             try:
#                 cardPrice.append(json_file['cardPrice']['value'])
#             except:
#                 cardPrice.append(nothing)
#
#             try:
#                 regularPrice.append(json_file['regularPrice']['value'])
#             except:
#                 regularPrice.append(nothing)
#
#             try:
#                 sku.append(json_file['code'])
#             except:
#                 sku.append(nothing)
#
#             try:
#                 link_small_img.append(json_file['shareSkuMetaImageUrl'])
#             except:
#                 link_small_img.append(nothing)
#
#             try:
#                 many.append(json_file['stock'])
#             except:
#                 many.append(nothing)
#
#             try:
#                 stockValue.append(json_file['stockValue'])
#             except:
#                 stockValue.append(nothing)
#
#             try:
#                 storeAddress.append(json_file['storeAddress'])
#             except:
#                 storeAddress.append(nothing)
#
#             try:
#                 title.append(json_file['title'])
#             except:
#                 title.append(nothing)
#
#             try:
#                 subTitle.append(json_file['subTitle'])
#             except:
#                 subTitle.append(nothing)
#
#             try:
#                 img_urls.append(', '.join([item['full'] for item in json_file['imageUrls']]))
#             except:
#                 img_urls.append(nothing)
#
#
#         except Exception as e:
#             print('Error', e)
#             all_in_one.append(nothing)
#             brend.append(nothing)
#             gacategory.append(nothing)
#             description.append(nothing)
#             cardPrice.append(nothing)
#             regularPrice.append(nothing)
#             sku.append(nothing)
#             link_small_img.append(nothing)
#             many.append(nothing)
#             stockValue.append(nothing)
#             storeAddress.append(nothing)
#             title.append(nothing)
#             subTitle.append(nothing)
#             img_urls.append(nothing)
#         link.append(url)
#
#     diction = {
#
#         'Категория': gacategory,
#         'Артикул': sku,
#         'Наименование': title,
#         'Подзаголовок': subTitle,
#         'Изображение товара': link_small_img,
#         'Ссылка на страницу': link,
#         'Обычная цена': regularPrice,
#         'Цена по акции': cardPrice,
#         'Склад': storeAddress,
#         'Кол-во ед': many,
#         'Кол-во': stockValue,
#         'Описание товара': description,
#         'Бренд': brend,
#         'Ссылки на фото': img_urls,
#         'Характеристики': all_in_one,
#     }
#     return diction
#
#
# def get_df_from_diction(diction):
#     try:
#         df = pd.DataFrame(diction)
#         df['Страна'] = df['Подзаголовок'].apply(lambda x: x.split(',')[0] if ',' in x else x)
#
#         today = datetime.datetime.now()
#         date_time = today.strftime("%Y%m%d_%H-%M")
#         filename = df['Категория'][0].split('/')[0] + '_' + date_time + '.xlsx'
#         df.to_excel(filename, index=False)
#     except Exception as e:
#         print('Не удалось сохранить df изза ошибки\n', e)
#
#
# if __name__ == '__main__':
#     freeze_support()
#     get_links_from_pages(all_links)
#     # prosto_dict = get_dict_from_links('links.txt', limit=5)
#     # get_df_from_diction(prosto_dict)
#


from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import datetime
import requests
import json
import time
import ast

domen = 'https://lenta.com'
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
driver = uc.Chrome(options=options)
driver.get(domen)

all_links = [
    #     'https://lenta.com/catalog/bakaleya/',
    #     'https://lenta.com/catalog/chajj-kofe-kakao/',
    #         'https://lenta.com/catalog/zdorovoe-pitanie/',
    'https://lenta.com/catalog/krasota-i-zdorove/',
    #     'https://lenta.com/catalog/bytovaya-himiya/',
    #     'https://lenta.com/catalog/sport-i-aktivnyjj-otdyh/',
    #     'https://lenta.com/catalog/tovary-dlya-zhivotnyh/',
    #     'https://lenta.com/catalog/lenta-zoomarket---professionalnyjj-uhod/',
    #     'https://lenta.com/catalog/avtotovary/',
]


def get_links_from_pages(all_links):
    for i, url in enumerate(all_links):
        print(f'{i + 1} из {len(all_links)}  {url}')
        file_name_txt = f"{url.split('/')[-2]}.txt"
        file_name_xlsx = f"{url.split('/')[-2]}.xlsx"

        driver.get(url)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        time.sleep(4)
        #         last_page_num = int(soup.find_all('li', class_='pagination__item')[-1].text)
        last_page_num = 166

        links = []

        for page_num in range(1, last_page_num + 1):
            url2 = f'{url}?page={page_num}'
            print(url2)
            try:
                driver.get(url2)
                time.sleep(3)
                driver.execute_script("window.scrollTo(0, 1000)")
                time.sleep(0.5)

                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                links += [domen + item.a['href'] for item in soup.find_all('div', class_='sku-card-small-container')]
                print(len(links))
                if len(links) == 0:
                    break
            except:
                pass

        links = sorted(set(links))
        print(f'Найдено {len(links)} товаров')

    file_name_txt = f"{all_links[0].split('/')[-2]}.txt"
    file_name_xlsx = f"{all_links[0].split('/')[-2]}.xlsx"
    with open(file_name_txt, "w") as f:
        try:
            f.write(str(links))
        except:
            print(f"Не удалось записать файл {file_name_txt}")
    return links


def get_dict_from_links(input_list, limit=5):
    nothing = 'missing'

    if type(input_list) == str:
        with open(input_list, "r") as f:
            links = ast.literal_eval(f.read())
        #     elif type(links) != list:
    #         break

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

    for idx, url in enumerate(links):
        if idx == limit:
            print(f'Лимит {limit} достигнут, прерываю...')
            break
        print(f'{idx + 1} из {len(links)}  {url}')
        try:
            driver.get(url)
            time.sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            json_file = json.loads(
                soup.find('div', class_='sku-page-control-container sku-page__control')['data-model'])
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
    return diction


def get_df_from_diction(diction):
    try:
        df = pd.DataFrame(diction)
        df['Страна'] = df['Подзаголовок'].apply(lambda x: x.split(',')[0] if ',' in x else x)

        today = datetime.datetime.now()
        date_time = today.strftime("%Y%m%d_%H-%M")
        filename = df['Категория'][0].split('/')[0] + '_' + date_time + '.xlsx'
        df.to_excel(filename, index=False)
    except Exception as e:
        print('Не удалось сохранить df изза ошибки\n', e)


get_links_from_pages(all_links)

bakaleya_dict = get_dict_from_links('bakaleya.txt', limit=10)
get_df_from_diction(bakaleya_dict)
