from deepface import DeepFace
import os

def validar_identidad():
    carpeta_imagenes = "TPOPENCV_2/Caras"
    archivos = os.listdir(carpeta_imagenes)
    imagen_referencia = "TPOPENCV_2/captura.jpg"

    for archivo in archivos:
        imagen_actual = os.path.join(carpeta_imagenes, archivo)

        try: 
            validacion = DeepFace.verify(img1_path=imagen_referencia, img2_path=imagen_actual)["verified"]
            if validacion:
                print("Usuario Valido.")
                return True
        except Exception as e:
            print(f"Rostro no encontrado para {archivo}")

    return False