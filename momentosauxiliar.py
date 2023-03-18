# FUNCIÓN PARA CALCULAR LOS MOMENTOS DE UNA IMAGEN
import sys
import cv2
import csv

def momentos(img):
    im = cv2.imread(img, 0)
    # crea la imagen binaria
    ret,thresh = cv2.threshold(im,127,255,0)
    # crea los contornos en la imagen
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    # crea matriz numérica de los puntos de contorno del objeto
    cnt = contours[0]
    # calcula los momentos
    M = cv2.moments(cnt)
    # creamos lista con los nombres de los momentos para la cabecera del csv
    header = list(M.keys())
    # creamos lista con los valores de los momentos para las filas del csv
    values = list(M.values())
    # creamos lista vacía para añadir la cabecera en caso de que exista un csv o dejarla vacía en caso contrario
    column_names = []
    try:
        # intentamos abrir el csv en modo lectura
        with open('/Users/alexiacazon/Documents/momentos.csv', 'r') as f1:
            # leemos csv
            reader = csv.DictReader(f1)
            # guardamos un diccionario con las entradas del csv
            dict_from_csv = dict(list(reader)[0])
            # guardamos la cabecera del csv existente
            column_names = list(dict_from_csv.keys())
    except:
        # excepción de que no exista el csv entonces explicamos que pasamos al siguiente paso en el que lo crearemos
        print("creamos csv")
    try:
        # intentamos escribir el csv
        if column_names==[]:
            # caso en el que no existe csv, creamos uno en modo escritura
            with open('/Users/alexiacazon/Documents/momentos.csv', 'w') as f2:
                # creamos el objeto escritura de diccionario
                dictwriter = csv.DictWriter(f2, fieldnames=header)
                # añadimos la cabecera con los nombres de los momentos
                dictwriter.writeheader()
                # escribimos el diccionario con los valores de los momentos
                dictwriter.writerow(M)
                # cerramos csv
                f2.close()
        else:
            # caso en el que si existe csv, lo abrimos en modo añadir datos
            with open('/Users/alexiacazon/Documents/momentos.csv', 'a') as f3:
                # creamos el objeto escritura
                writer = csv.writer(f3)
                # añadimos valores de los nuevos momentos
                writer.writerow(values)
                # cerramos csv
                f3.close()

    except IOError:
        # excepción de que ha habido un error en el proceso de la escritura del csv
        print("I/O error")

def stegomomentos(stegoimg):
    # lee la imagen
    im = cv2.imread(stegoimg, 0)
    # crea la imagen binaria
    ret,thresh = cv2.threshold(im,127,255,0)
    # crea los contornos en la imagen
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    # crea matriz numérica de los puntos de contorno del objeto
    cnt = contours[0]
    # calcula los momentos
    M = cv2.moments(cnt)
    # creamos lista con los nombres de los momentos para la cabecera del csv
    header = list(M.keys())
    # creamos lista con los valores de los momentos para las filas del csv
    values = list(M.values())
    # creamos lista vacía para añadir la cabecera en caso de que exista un csv o dejarla vacía en caso contrario
    column_names = []
    try:
        # intentamos abrir el csv en modo lectura
        with open('/Users/alexiacazon/Documents/stegomomentos.csv', 'r') as f1:
            # leemos csv
            reader = csv.DictReader(f1)
            # guardamos un diccionario con las entradas del csv
            dict_from_csv = dict(list(reader)[0])
            # guardamos la cabecera del csv existente
            column_names = list(dict_from_csv.keys())
    except:
        # excepción de que no exista el csv entonces explicamos que pasamos al siguiente paso en el que lo crearemos
        print("creamos csv")
    try:
        # intentamos escribir el csv
        if column_names==[]:
            # caso en el que no existe csv, creamos uno en modo escritura
            with open('/Users/alexiacazon/Documents/stegomomentos.csv', 'w') as f2:
                # creamos el objeto escritura de diccionario
                dictwriter = csv.DictWriter(f2, fieldnames=header)
                # añadimos la cabecera con los nombres de los momentos
                dictwriter.writeheader()
                # escribimos el diccionario con los valores de los momentos
                dictwriter.writerow(M)
                # cerramos csv
                f2.close()
        else:
            # caso en el que si existe csv, lo abrimos en modo añadir datos
            with open('/Users/alexiacazon/Documents/stegomomentos.csv', 'a') as f3:
                # creamos el objeto escritura
                writer = csv.writer(f3)
                # añadimos valores de los nuevos momentos
                writer.writerow(values)
                # cerramos csv
                f3.close()

    except IOError:
        # excepción de que ha habido un error en el proceso de la escritura del csv
        print("I/O error")