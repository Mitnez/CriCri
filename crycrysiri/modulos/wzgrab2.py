try:
    from os import pardir
    import pyshark
    import modulos.parseadorips as paip
except:
    print("Algun modulo no esta descargado")

def parses():
    print("===========================================")
    print("Recolectando datos :D")
    cap = pyshark.LiveCapture(output_file='Data\\logs.pcap', interface='\\Device\\NPF_{D567F107-29CB-4DB0-B41E-4C719F129B9D}')
    cap.sniff(timeout=20)
    print("===========================================")
    print("IPs encontradas :D")
    paip.parseador()
    exit()
if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")