from PIL import Image
import os
import cv2

input_images_path = "/Users/alexiacazon/Desktop/imagenespng"
files_names = os.listdir(input_images_path)
output_images_path = "/Users/alexiacazon/Desktop/stego-imagenes"


os.system("cd /Users/alexiacazon/Desktop/Steganography")
for file_name in files_names:
    output_file_name = "stego-" + file_name
    output_image_path = output_images_path + "/" + output_file_name
    image_path = input_images_path + "/" + file_name
    message_path = "/Users/alexiacazon/Desktop/mensaje.txt"
    comando = "stegolsb steglsb -h -i " + image_path + " -s " + message_path + " -o " + output_image_path + " -c 1"
    #print(comando)
    os.system(comando)