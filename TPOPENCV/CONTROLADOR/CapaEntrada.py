import cv2 as cv
import os
#ruidos = cv.CascadeClassifier("D:\Soporte\practicos\G2310\TPOPENCV\CONTROLADOR\haarcascade_frontalface_default.xml")
camara= cv.VideoCapture(0)

def CapturarRostro(user):
    id=0
    ruidos = cv.CascadeClassifier("D:\Soporte\practicos\G2310\TPOPENCV\CONTROLADOR\haarcascade_frontalface_default.xml")
    ruta = "D:/Soporte/practicos/G2310/TPOPENCV/FOTOS/"+str(user)+"/"
    camara= cv.VideoCapture(0)
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    while True:
        grises=cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
        idcaptura=camara.copy()

        cara=ruidos.detectMultiScale(grises,1.3,5)
        for(x,y,e1,e2) in cara:
            cv.rectangle(camara,(x,y),(x+e1,y+e2),(255,0,0),2)
            rostrocapturado=idcaptura[y:y+e2 ,x:x+e1]
            rostrocapturado=cv.resize(rostrocapturado, (160,160),interpolation=cv.INTER_CUBIC)
            cv.imwrite(ruta+"/imagen_{}.jpg".format(id), rostrocapturado)
            id=id+1
        if id==151:
            break
    cv.imshow("Resultado rostro", camara)
    camara.release()
    cv.destroyAllWindows()

        