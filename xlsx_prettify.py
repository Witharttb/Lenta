import xlsxwriter
png_path = r'C:\Users\Sergei\PycharmProjects\Parsing\Lenta\pics\preview\46\69\33\162142.png'
png_path2 = r'C:\Users\Sergei\PycharmProjects\Parsing\Lenta\pics\preview\46\69\34\280093.png'

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('images.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 30)

# Insert an image with scaling and offset.
worksheet.write('A29', 'Insert a scaled image:')
worksheet.insert_image('B29', png_path2, {'x_scale': 4, 'y_scale': 4, 'x_offset': 15, 'y_offset': 10})

workbook.close()