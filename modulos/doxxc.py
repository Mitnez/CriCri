import os
import wget

from modulos import utilidades as u


def main():
    u.limpiar_consola()
    u.logo("DoxxCETI", "big")
    registro = input("Ingresa el registro a buscar => ")
    url = "https://tonala.ceti.mx/modulos/alumnos/pdf/horario/"+registro
    ruta = "data\\" + registro + ".pdf"
    wget.download(url, ruta)
    print("Descargado :D")
    os.system(ruta)


if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")