import urllib.request
import json

class geo():
    def geolocalizacion(sacada):
        ip = sacada
        url = "https://ipinfo.io/" + ip + "/json"
        abrirURL = urllib.request.urlopen(url)
        cargarURL = json.load(abrirURL)
        print("Esto es lo que encontre :D\n")
        for i in cargarURL:
            print( i + ": " + cargarURL[i])

if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")