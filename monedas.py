import cv2
import matplotlib.pyplot as plt
import numpy as np

#Tratamiento previo de la imagen
img1 = cv2.imread('monedas.jpg')
img1 = cv2.resize(img1, (0, 0), fx=0.2, fy=0.2)  # para ajustar el tamaño
img1 = cv2.GaussianBlur(img1, (7, 7), 0)  # para suavizar la imagen

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  #Convertir de BGR a RGB
img1_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY) #Convertir de RGB a GRIS


