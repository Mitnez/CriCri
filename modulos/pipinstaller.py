import subprocess
import sys
import os

class instalador():
    def instaladorpip (paquete):
        a = open(os.devnull, 'w')
        print("Instalando el modulo bs4 :D")
        p = subprocess.call([sys.executable, "-m", "pip", "install", paquete], stdout=a, stderr=subprocess.STDOUT)
        if p == 0:
            print("El modulo fue instalado bn")
        else:
            print("No sirve o no hay internet")