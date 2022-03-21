import json
import urllib.request

from modulos import utilidades as u


def geolocalizacion():
    u.logo("InfoIP", "big")
    ip = input("Introduce una direccion IP ==> ")
    url = "https://ipinfo.io/" + ip + "/json"
    abrirURL = urllib.request.urlopen(url)
    cargarURL = json.load(abrirURL)
    print("Esto es lo que encontre :D\n")
    for i in cargarURL:
        print(i + ": " + cargarURL[i])


def geolo(sacada):
    ip = sacada
    url = "https://ipinfo.io/" + ip + "/json"
    abrirURL = urllib.request.urlopen(url)
    cargarURL = json.load(abrirURL)
    info = cargarURL["org"] + " " + cargarURL["country"] + " " + cargarURL["region"]
    return info


if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")
