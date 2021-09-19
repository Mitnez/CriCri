try:
    from os import pardir
    import pyshark
    import modulos.parseadorips as paip
    import subprocess
except:
    print("Alguno modulo no esta descargado o en la raíz de CryCry")

def parses():
    print("")
    print("========INTERFACES DE RED========")
    subprocess.call(
    [r'modulos\\tshark.bat'])
    print("=================================")
    moduloinalambrico = input("Ingresa la ruta de la interfaz de red (SIN EL NOMBRE, SOLO LA RUTA HASTA EL }) \n ==> ")
    print("===========================================")
    print("Recolectando datos :D")
    cap = pyshark.LiveCapture(output_file='Data\\logs.pcap', interface=moduloinalambrico)
    cap.sniff(timeout=20)
    print("===========================================")
    print("IPs encontradas :D")
    paip.parseador()
    exit()

if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")
