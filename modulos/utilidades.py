import os
import sys
from pyfiglet import figlet_format

def logo(titulo, fuente):
        print(figlet_format(titulo, font=fuente))

def limpiar_consola():
        comando = 'clear'
        if os.name in ('nt', 'dos'):
            comando = 'cls'
            os.system(comando)
    
def detector_de_sistema():
        if "linux" in sys.platform:
            print("Corriendo CryCry en Linux")
            return "linux"
        elif "darwin" in sys.platform:
            print("Corriendo CryCry en macOS")
            return "macos"
        elif "win" in sys.platform:
            print("Corriendo CryCry en Windows")
            return "windows"
        else:
            print("No se cual sea el sistema {}, si funciona que cool la verdad".format(sys.platform))