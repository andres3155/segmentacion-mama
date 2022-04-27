from os import environ
import cv2 
import numpy as np 
from matplotlib import pyplot as plt

################### comando para arreglar visual ###################
environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"
####################################################################

img = cv2.imread('D:\DECIMO_SEMESTRE_INGENIERIA_ELECTRONICA\TRABAJO DE GRADO\IN_MIAS_PRUEBA\mdb(13).pgm', cv2.IMREAD_GRAYSCALE)
#se guarada en variables cual es el ancho y el alto de la imagen original
height = img.shape[0]
width = img.shape[1]

# se redimencionada la imagen usando una interpolación cubica
image = cv2.resize(img, (700, 500), interpolation=cv2.INTER_CUBIC)

#se guarada en variables cual es el ancho y el alto de la imagen original
height_new = image.shape[0]
width_new = image.shape[1]

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
histogramaH = np.sum(image, axis=0)



if histogramaH[20] < 20000:
    image_inver= cv2.flip(image,1)

if histogramaH[20] < 20000:
    image_inver= cv2.flip(image,1)
    histogramaH_inver = np.sum(image_inver, axis=0)

    print("se hizo la rotación")

    print("se hizo la rotación")

    # Se grafican los histogramas en una figura.
    fig, Hisplt=plt.subplots(2,2)
    Hisplt[0,0].imshow(image,cmap='gray' )
    Hisplt[0,0].set_title('Imagen '+ 'W: '+ str(width_new) + ' H: ' + str(height_new),fontweight='bold' )
    Hisplt[0,0].axis('off')   

    Hisplt[0,1].plot(histogramaH, color ='#000000' )
    Hisplt[0,1].set_title('Histograma Horizontal',fontweight='bold')
    Hisplt[0,1].set_xlabel('Number of pixel',fontweight='bold')
    Hisplt[0,1].set_ylabel('Gray nivel',fontweight='bold')

    Hisplt[1,1].plot(histogramaH_inver, color = '#000000')
    Hisplt[1,1].set_title('Histograma Horizontal',fontweight='bold')
    Hisplt[1,1].set_xlabel('Number of pixel',fontweight='bold')
    Hisplt[1,1].set_ylabel('Comulativa sum of gray',fontweight='bold')

    Hisplt[1,0].imshow(image_inver,cmap='gray' )
    Hisplt[1,0].set_title('Imagen '+ 'W: '+ str(width_new) + ' H: ' + str(height_new),fontweight='bold' )
    Hisplt[1,0].axis('off')

    # Configuración para acomodar las gráficas 
    fig.tight_layout() 
    fig.canvas.set_window_title('Histogramas')
    # Graficar
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No se hizo la rotación")
    # Se grafican los histogramas en una figura.
    fig, Hisplt=plt.subplots(2,2)
    Hisplt[0,0].imshow(image,cmap='gray' )
    Hisplt[0,0].set_title('Imagen '+ 'W: '+ str(width_new) + ' H: ' + str(height_new),fontweight='bold' )
    Hisplt[0,0].axis('off')   

    Hisplt[0,1].plot(histogramaH, color ='#000000' )
    Hisplt[0,1].set_title('Histograma Horizontal',fontweight='bold')
    Hisplt[0,1].set_xlabel('Number of pixel',fontweight='bold')
    Hisplt[0,1].set_ylabel('Gray nivel',fontweight='bold')

    # Configuración para acomodar las gráficas 
    fig.tight_layout() 
    fig.canvas.set_window_title('Histogramas')
    # Graficar
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


