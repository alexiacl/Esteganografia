from PIL import Image
import os
import cv2

input_images_path = "/Users/alexiacazon/Desktop/imagenes"
files_names = os.listdir(input_images_path)
output_images_path = "imagenespng"

if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)

for file_name in files_names:
    if file_name.split(".")[-1] not in ["jpeg", "png"]:
        file_name2 = file_name.split(".")[0] + ".png"
    image_path = input_images_path + "/" + file_name
    image_path2 = output_images_path + "/" + file_name2
    im1 = Image.open(image_path)
    im1.save(image_path2)