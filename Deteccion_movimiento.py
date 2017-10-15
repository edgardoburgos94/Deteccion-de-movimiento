import numpy as np
import cv2
import time
import smtplib

cap = cv2.VideoCapture(0)  #Inicializar cámara
tiempo = 0.1

_,img1 = cap.read()  #Tomar primera foto
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #Convertir imagen a escala de grises
while (True):

    #CAMBIO EN 1 x TIEMPO
    time.sleep (tiempo) # Espera el tiempo determinado
    _, img2o = cap.read()  #Tomar foto
    img2 = cv2.cvtColor(img2o, cv2.COLOR_BGR2GRAY) #Convertir imagen a escala de grises
    img2=np.array(img2,np.float32) #Convertir imagen a float32 para operarlas
    img1=np.array(img1,np.float32) #Convertir imagen a float32 para operarlas
    dif = np.array(abs(img1-img2),np.uint8) #Restar imagenes
    ret,bina = cv2.threshold(dif,50,255,cv2.THRESH_BINARY) # Binarizar la imagen
                              # Encontrar área máxima
    x,y,w,h=cv2.boundingRect(bina)
    area_max1=w*h
    #print(w*h)
    cv2.rectangle(img2o,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Flow',dif)#Ver diferencia imagenes
    cv2.imshow('Original',img2o)#Ver diferencia imagenes

    #CAMBIO EN 2 x TIEMPO
    time.sleep (tiempo) # Espera el tiempo determinado
    _, img3o = cap.read()  #Tomar foto
    img3 = cv2.cvtColor(img3o, cv2.COLOR_BGR2GRAY) #Convertir imagen a escala de grises
    img3=np.array(img3,np.float32) #Convertir imagen a float32 para operarlas
    dif = np.array(abs(img1-img3),np.uint8) #Restar imagenes
    ret,bina = cv2.threshold(dif,50,255,cv2.THRESH_BINARY) # Binarizar la imagen
                              # Encontrar área máxima
    x,y,w,h=cv2.boundingRect(bina)
    area_max2=w*h
    #print(w*h)
    cv2.rectangle(img3o,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Flow',dif)#Ver diferencia imagenes
    cv2.imshow('Binarización',bina)#Ver diferencia imagenes
    cv2.imshow('Original',img3o)#Ver diferencia imagenes

    #CAMBIO EN 3 x TIEMPO
    time.sleep (tiempo) # Espera el tiempo determinado
    _, img4o = cap.read()  #Tomar foto
    img4 = cv2.cvtColor(img4o, cv2.COLOR_BGR2GRAY) #Convertir imagen a escala de grises
    img4 = np.array(img4,np.float32) #Convertir imagen a float32 para operarlas
    dif = np.array(abs(img1-img4),np.uint8) #Restar imagenes
    ret,bina = cv2.threshold(dif,50,255,cv2.THRESH_BINARY) # Binarizar la imagen
                              # Encontrar área máxima
    x,y,w,h=cv2.boundingRect(bina)
    area_max3=w*h
    #print(w*h)
    cv2.rectangle(img4o,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Flow',dif) #Ver diferencia imagenes
    cv2.imshow('Binarización',bina)#Ver diferencia imagenes
    cv2.imshow('Original',img4o)#Ver diferencia imagenes

    img1 = img2 #Actualizar imagen anterior

    arreglo = np.matrix([area_max1,area_max2,area_max3])
    area_dif = arreglo.max()

    if area_dif > 250000:
        #ENVIAR CORREO
        content = 'ATENCION, Deteccion de movimiento camara cuarto activada'
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('edgardo.burgos94@gmail.com','e1d9b9a4')
        mail.sendmail('edgardo.burgos94@gmail.com','edgardo.burgos94@gmail.com',content)
        mail.close()
        print("Correo enviado")

    print(area_dif)

    # CERRAR CICLO CUANDO SE PRESIONE "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Mostrar dimensiones de la im1
print(img1.shape)

cap.release()
cv2.destroyAllWindows()
