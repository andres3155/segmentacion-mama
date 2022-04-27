import cv2
import numpy as np

#se define la funcion la cual sirve para realizar el filtro espacial 
def gamma_trans(img,gamma):
	 # El método específico se normaliza primero a 1, y luego se usa gamma como valor de índice para encontrar el nuevo valor de píxel y luego restaurar
	gamma_table = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
	gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
	 # La implementación de mapeo utiliza la función de búsqueda de tablas de Opencv
	return cv2.LUT(img,gamma_table)

#se define la funcion la cual es la que nos sirve para quitar los objetos de la imagen no deseados 
def bwareaopen(imag_seg, min_size, connectivity=8):
        # Encuentre todos los componentes conectados (llamados aquí "etiquetas")
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            imag_seg, connectivity=connectivity)
        
        # comprobar el tamaño de todos los componentes conectados (área en píxeles)
        for i in range(num_labels):
            label_size = stats[i, cv2.CC_STAT_AREA]
            
            # eliminar componentes conectados más pequeños que min_size
            if label_size < min_size:
                imag_seg[labels == i] = 0
                
        return imag_seg

#se define la funcion la cual es la que nos sirve para detectar los bordes de las imagenes
def segcanny(imag_seg):

    # Aplicar suavizado Gaussiano
    gauss = cv2.GaussianBlur(imag_seg, (5,5), 0)
    # Detectamos los bordes con Canny
    canny = cv2.Canny(gauss, 50, 150)
    # Buscamos los contornos
    (contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #se crea la mascara con los contornos
    mascara = cv2.drawContours(imag_seg,contornos,-1,(0,0,255), 2)

    return mascara
