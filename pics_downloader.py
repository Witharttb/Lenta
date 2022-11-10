import requests
from pathlib import Path
import pandas as pd
import os
import openpyxl

xlsx_path = 'Здоровое питание_20221110_11-53.xlsx'


def get_pics_from_urls(path_to_xlsx):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    # Download photos
    df = pd.read_excel(path_to_xlsx)[['Артикул', 'Изображение товара']]
    for idx, item in df.iterrows():
        print(f'{idx + 1} из {len(df.index)}')
        sku = str(df["Артикул"][idx])
        img_name = df["Изображение товара"][idx].split('?')[0].split('/')[-1]
        folder_name = f'pics/preview/{sku[:2]}/{sku[2:4]}/{sku[4:]}'
        image_url = df["Изображение товара"][idx]
        if not os.path.exists(folder_name + '/' + img_name):  # Если файл еще не скачан
            Path(folder_name).mkdir(parents=True, exist_ok=True)
            response = requests.get(image_url, headers=headers)
            if response.status_code:
                fp = open(folder_name + '/' + img_name, 'wb')
                fp.write(response.content)
                fp.close()
                print(image_url, 'ok')
            else:
                print(image_url, 'не доступен')


get_pics_from_urls(xlsx_path)
