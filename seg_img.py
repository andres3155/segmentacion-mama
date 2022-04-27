from os import environ
import cv2
import numpy as np
import func_tecnicas_seg as fts

################### comando para arreglar visual ################### 
environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"
####################################################################

#leemos la imagen 
img = cv2.imread('D:\DECIMO_SEMESTRE_INGENIERIA_ELECTRONICA\TRABAJO DE GRADO\IN_MIAS_PRUEBA\mdb(12).pgm', cv2.IMREAD_GRAYSCALE)
#se guarada en variables cual es el ancho y el alto de la imagen original
height = img.shape[0]
width = img.shape[1]

# se redimencionada la imagen usando una interpolación cubica
image = cv2.resize(img, (700, 500), interpolation=cv2.INTER_CUBIC)

#se guarada en variables cual es el ancho y el alto de 
# la imagen original
height_new = image.shape[0]
width_new = image.shape[1]

#se llama la fucinon gamma_trans y se realiza el filtro
image_corrted = fts.gamma_trans(image, 0.2)

# suavisado de la imagen 
kernel = np.ones((5,5),np.float32)/25#Crea el kernel
dst = cv2.filter2D(image_corrted,-1,kernel)#Filtra la imagen utilizando el kernel anterior

#se binariza la imagen 
ret,imag_binar = cv2.threshold(dst,127,255,cv2.THRESH_BINARY) #135 127

#se llama la funcion bwareaopen para quitar artefactos de la imagen 
imag_seg = fts.bwareaopen(imag_binar,40000,connectivity=8)#29436 es el limite para quitar los artefactos de esta imagen 150

#se llama la funcion segcanny para aplica deteccion de bordes con la tecnica canny
img_seg_canny = fts.segcanny(imag_seg)

img_segmentada = img_seg_canny * (255-image)

cv2.imshow("img segmentada", img_segmentada)
cv2.waitKey(0)
cv2.destroyAllWindows()