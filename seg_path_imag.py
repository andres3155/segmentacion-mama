import cv2 
import os
import matplotlib as mtl
from matplotlib import pyplot as plt

def imageFunctionProcessing(path):

    img = cv2.imread(path,cv2.COLOR_BGR2RGB)

    return img


#in_PATH = 'C:\\Users\\danie\Desktop\\Base_datos\\benign\\'
#outh_PATH = 'C:\\Users\danie\\Desktop\\Base_datos\\bening_modificado\\'
in_PATH = 'D:\\DECIMO_SEMESTRE_INGENIERIA_ELECTRONICA\\TRABAJO DE GRADO\\IN_MIAS_PRUEBA\\'
outh_PATH = 'D:\\DECIMO_SEMESTRE_INGENIERIA_ELECTRONICA\\TRABAJO DE GRADO\\OUT_MIAS_PRUEBA\\'

#name_image_input = 'Benign_ ({0}).jpg'
#name_image_output ='Benign_ ({0})_seg.jpg'

name_image_input = 'mdb({0}).pgm'
name_image_output ='mdb_({0})_seg.pgm'

# in_PATH = 'C:\\Users\\danie\Desktop\\Base_datos\\malignant\\'
# outh_PATH = 'C:\\Users\danie\\Desktop\\Base_datos\\malignant_modificado\\'
# name_image_input = 'malignant_ ({0}).jpg'
# name_image_output ='malignant_ ({0})_seg.jpg'

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

#Verificando 
#print(len(file_names_images))
#print(file_names_images[0])


# Redimensionando la imagenes en 224 x 244 para estandarizar y convirtiendo a escala de grises 
output_images_path = outh_PATH
#Tamaño_final_Dataset = 100

for i in range(initial_count):
    imageFinal= imageFunctionProcessing(file_names_images[i])
    cv2.imwrite(output_images_path  + name_image_output.format(i+1), imageFinal)