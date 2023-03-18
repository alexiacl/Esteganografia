import csv
import random
import os
from momentosauxiliar import *

images_path = "/Users/alexiacazon/Desktop/imagenes"
stegoimages_path = "/Users/alexiacazon/Desktop/stego-imagenes"
images_names = os.listdir(images_path)
stegoimages_names = os.listdir(stegoimages_path)

for image_name in images_names:
    img = images_path+ "/"+image_name
    momentos(img)
for stegoimage_name in stegoimages_names:
    stegoimg = stegoimages_path+ "/"+ stegoimage_name
    if stegoimg!="/Users/alexiacazon/Desktop/stego-imagenes/.DS_Store":
        stegomomentos(stegoimg)

with open('/Users/alexiacazon/Documents/momentos.csv', 'r') as f1:
    with open('/Users/alexiacazon/Documents/stegomomentos.csv', 'r') as f2:
        reader = csv.reader(f1)
        list_from_csv = list(reader)
        lista = []
        reader2 = csv.reader(f2)
        list_from_csv2 = list(reader2)
        for row in list_from_csv:
            if row[0]=='m00':
                row.append('output')
                lista.append(row)
            else:
                row.append('0')
                lista.append(row)
        for row2 in list_from_csv2:
            if row2[0]!='m00':
                row2.append('1')
                lista.append(row2)
        with open('/Users/alexiacazon/Documents/momentosfinales.csv', 'w') as f3:
            writer = csv.writer(f3)
            random.shuffle(lista)
            for row in lista:
                if row == ['m00', 'm10', 'm01', 'm20', 'm11', 'm02', 'm30', 'm21', 'm12', 'm03', 'mu20', 'mu11', 'mu02', 'mu30', 'mu21', 'mu12', 'mu03', 'nu20', 'nu11', 'nu02', 'nu30', 'nu21', 'nu12', 'nu03', 'output']:
                    writer.writerow(row)
            for row in lista:
                if row != ['m00', 'm10', 'm01', 'm20', 'm11', 'm02', 'm30', 'm21', 'm12', 'm03', 'mu20', 'mu11', 'mu02', 'mu30', 'mu21', 'mu12', 'mu03', 'nu20', 'nu11', 'nu02', 'nu30', 'nu21', 'nu12', 'nu03', 'output']:
                    writer.writerow(row) 
            f3.close()
