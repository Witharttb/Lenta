import requests
from pathlib import Path
import pandas as pd
import os
import openpyxl
from PIL import Image
from resizeimage import resizeimage

xlsx_path = 'Красота и здоровье_20221110_22-32.xlsx'


def get_pics_from_urls(path_to_xlsx):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    # Download photos
    df = pd.read_excel(path_to_xlsx)[['Артикул', 'Изображение товара']]
    for idx, item in df.iterrows():
        if 'missing' not in df["Изображение товара"][idx]:
            print(f'{idx + 1} из {len(df.index)}', end=' ')
            sku = str(df["Артикул"][idx])
            img_name = df["Изображение товара"][idx].split('?')[0].split('/')[-1]
            folder_name = f'pics/preview/{sku[:2]}/{sku[2:4]}/{sku[4:]}'
            image_url = df["Изображение товара"][idx]
            if not os.path.exists(folder_name + '/' + img_name):  # Если файл еще не скачан
                Path(folder_name).mkdir(parents=True, exist_ok=True)
                try:
                    response = requests.get(image_url, headers=headers)

                    if response.status_code == 200:
                        fp = open(folder_name + '/' + img_name, 'wb')
                        fp.write(response.content)
                        fp.close()
                        print(image_url, 'ok')
                    else:
                        print(image_url, 'не доступен')
                except:
                    print(image_url, 'Не работает')


def image_resize(path_to_xlsx):
    df = pd.read_excel(path_to_xlsx)[['Артикул', 'Изображение товара']]
    for idx, item in df.iterrows():
        if 'missing' not in df["Изображение товара"][idx]:
            print(f'{idx + 1} из {len(df.index)}')
            sku = str(df["Артикул"][idx])
            img_name = df["Изображение товара"][idx].split('?')[0].split('/')[-1]
            folder_name = f'pics/preview/{sku[:2]}/{sku[2:4]}/{sku[4:]}'
            folder_name_thumbs = f'pics/thumbs/{sku[:2]}/{sku[2:4]}/{sku[4:]}'

            try:
                fd_img = open(folder_name + '/' + img_name, 'rb')
                img = Image.open(fd_img)
                img = resizeimage.resize('thumbnail', img, [200, 200])
                Path(folder_name_thumbs).mkdir(parents=True, exist_ok=True)
                img.save(folder_name_thumbs + '/' + img_name, img.format)
                fd_img.close()

            except Exception as e:
                print(img_name, e)


get_pics_from_urls(xlsx_path)
image_resize(xlsx_path)
