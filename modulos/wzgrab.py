from alive_progress import alive_bar

try:
    from os import pardir
    import sys, subprocess, pyshark
    from alive_progress import config_handler
    from modulos import parseadorips as paip, loading, utilidades as u
except:
    print("Alguno modulo no esta descargado o en la raíz de CryCry")


def inicio():
    u.logo("IP Grabber", "big")
    print("")
    print("========INTERFACES DE RED========")
    try:
        if 'win' in sys.platform:
            subprocess.call([r'modulos\\tshark.bat'])
        elif 'linux' in sys.platform:
            subprocess.run(['tshark', '-D'])
    except:
        #  if 'linux' in sys.platform:
        #     print("Tienes linux, genial :D")
        #    subprocess.run(['tshark -D'])
        # else:
        #    print("Hubo un problema al correr el modulo en Windows")
        print("Hubo un problema al llamar a TShark, verifica la ruta")
    print("=================================")
    moduloinalambrico = input("Ingresa la ruta de la interfaz de red (SIN EL NOMBRE, SOLO LA RUTA HASTA EL }) \n ==> ")
    print("===========================================")
    print("Recolectando datos :D")
    with alive_bar(total=None, bar='blocks'):
        cap = pyshark.LiveCapture(output_file='logs', interface=moduloinalambrico)
        cap.sniff(timeout=20)
    print("===========================================")
    print("IPs encontradas :D")
    paip.parseador()
    exit()


if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")
