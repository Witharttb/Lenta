import xlsxwriter
import imagesize
import time
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

xlsx_path = 'Здоровое питание_20221110_12-50.xlsx'
box_size = 60
offset = box_size / 8


def insert_pics(path_to_xlsx):
    df = pd.read_excel(path_to_xlsx)[['Артикул', 'Изображение товара']]

    workbook = xlsxwriter.Workbook('images.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column_pixels(0, 0, 400)
    worksheet.set_column_pixels(1, 1, box_size)
    for idx, item in df.iterrows():
        print(f'{idx + 1} из {len(df.index)}')
        sku = str(df["Артикул"][idx])
        img_name = df["Изображение товара"][idx].split('?')[0].split('/')[-1]
        folder_name = f'pics/thumbs/{sku[:2]}/{sku[2:4]}/{sku[4:]}'
        image_url = df["Изображение товара"][idx]
        worksheet.set_row_pixels(idx, box_size)
        # Insert an image with scaling and offset.
        worksheet.write(idx, 0, 'Insert a scaled image:')

        if 'missing' not in img_name:
            try:
                dpi_koef = 0.5
                png_path = folder_name + '/' + img_name
                width, height = imagesize.get(png_path)
                print(png_path, width, height)
                x_offset = ((60 - width) / 2) * dpi_koef
                y_offset = ((60 - height) / 2) * dpi_koef

                worksheet.insert_image(idx, 1, png_path,
                                       {'x_scale': 0.8, 'y_scale': 0.8,
                                        'x_offset': x_offset + offset,
                                        'y_offset': y_offset + offset})

                print(x_offset, width)
                print(y_offset, height)
            except:
                pass
    workbook.close()


def format_col_width(ws):
    ws.set_column('B:C', 20)
    ws.set_column('D:D', 1)
    ws.set_column('E:E', 20)


df = pd.read_excel(xlsx_path)
df['Изображение товара'] = ''

writer = pd.ExcelWriter("__"+xlsx_path, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
df = pd.read_excel(xlsx_path)[['Артикул', 'Изображение товара']]

workbook = writer.book
worksheet = writer.sheets['Sheet1']

# format_col_width(worksheet)

for idx, item in df.iterrows():
    print(f'{idx + 1} из {len(df.index)}')
    sku = str(df["Артикул"][idx])
    img_name = df["Изображение товара"][idx].split('?')[0].split('/')[-1]
    folder_name = f'pics/thumbs/{sku[:2]}/{sku[2:4]}/{sku[4:]}'
    image_url = df["Изображение товара"][idx]
    worksheet.set_row_pixels(idx+1, box_size)

    if 'missing' not in img_name:
        try:
            dpi_koef = 0.5
            png_path = folder_name + '/' + img_name
            width, height = imagesize.get(png_path)
            print(png_path, width, height)
            x_offset = ((60 - width) / 2) * dpi_koef
            y_offset = ((60 - height) / 2) * dpi_koef

            worksheet.insert_image(idx+1, 4, png_path,
                                   {'x_scale': 0.8, 'y_scale': 0.8,
                                    'x_offset': x_offset + offset,
                                    'y_offset': y_offset + offset})
        except:
            pass

writer.close()

# insert_pics(xlsx_path)
# add_pictures(xlsx_path)
