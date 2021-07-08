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
            print(3, "Corriendo CryCry en Linux")
            pass
        elif "darwin" in sys.platform:
            print(3, "Corriendo CryCry en macOS")
            pass
        elif "win" in sys.platform:
            print("Corriendo CryCry en Windows")
            sys.exit(1)
        else:
            print("No se cual sea el sistema {}, si funciona que cool la verdad".format(sys.platform))
        return 
