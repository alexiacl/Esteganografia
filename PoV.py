import cv2
import sys

def detectar_esteganografia(imagen):
    # Cargar la imagen
    img = cv2.imread(imagen)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calcular la matriz de correlación
    corr_matrix = cv2.matchTemplate(gray, gray, cv2.TM_CCORR_NORMED)

    # Calcular la media y la desviación estándar de la matriz de correlación
    mean = cv2.mean(corr_matrix)[0]
    std_dev = cv2.meanStdDev(corr_matrix)[1][0][0]

    # Comprobar si la desviación estándar es menor que un umbral
    # si es así, la imagen podría contener esteganografía
    print("p-valor", std_dev)
    if std_dev < 0.01:
        print("La imagen podría contener esteganografía.")
    else:
        print("La imagen parece ser normal.")

imagen = sys.argv[1]
detectar_esteganografia(imagen)







