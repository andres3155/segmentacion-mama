from os import environ
import os
import cv2
import numpy as np
import func_segmentacion as fs

################### comando para arreglar visual ################### 
environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"
####################################################################

in_PATH = 'D:\\DECIMO_SEMESTRE_INGENIERIA_ELECTRONICA\\TRABAJO DE GRADO\\IN_MIAS_PRUEBA\\'
outh_PATH = 'D:\\DECIMO_SEMESTRE_INGENIERIA_ELECTRONICA\\TRABAJO DE GRADO\\OUT_MIAS_PRUEBA\\'

name_image_input = 'mdb({0}).pgm'
name_image_output ='mdb_({0})_seg.pgm'

input_images_path = in_PATH


#CONTAMOS LA CANTIDAD DE IMAGENES EN LA CARPETA 
initial_count = 0
dir = input_images_path
file_names_images = []

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1
print(initial_count)

#Almacenando en un arreglo la direccion de las imagenes los nombres vienen dados por mdb .pgm desde 1
file_names_images = []
for i in range(initial_count):
  file_names_images.append(dir + name_image_input.format(i+1))

output_images_path = outh_PATH

for i in range(initial_count):
    imageFinal= fs.segimg(file_names_images[i])
    cv2.imwrite(output_images_path  + name_image_output.format(i+1), imageFinal)