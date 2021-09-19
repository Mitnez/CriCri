import os
import sys

def logo():
        print('''
     _____            _____                 __   _____ 
    /  __ \          /  __ \               /  | |  _  |
    | /  \/_ __ _   _| /  \/_ __ _   _     `| | | |/' |
    | |   | '__| | | | |   | '__| | | |     | | |  /| |
    | \__/| |  | |_| | \__/| |  | |_| |    _| |_\ |_/ /
    \____|_|   \__, |\____|_|   \__, |    \___(_\___/ 
                __/ |            __/ |                
               |___/            |___/                 
    \n
    ''')

def limpiar_consola():
        comando = 'clear'
        if os.name in ('nt', 'dos'):
            comando = 'cls'
            os.system(comando)
    
def detector_de_sistema():
        if "linux" in sys.platform:
            print("Corriendo CryCry en Linux")
        elif "darwin" in sys.platform:
            print("Corriendo CryCry en macOS")
        elif "win" in sys.platform:
            print("Corriendo CryCry en Windows")
        else:
            print("No se cual sea el sistema {}, si funciona que cool la verdad".format(sys.platform))