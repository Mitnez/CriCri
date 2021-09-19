try:
    from modulos.reverse import sitiosscan
    from modulos.geo import geo
    from modulos.selfip import ip
    import modulos.utilidades as utilidades
    import modulos.pipinstaller as pipinstaller
    import modulos.wzgrab as wzg
except:
    print("Uno o más modulos necesitan descargarse, comprueba el git o contacta a m1ttt.")

public = ip.ippublica()

def main():
    utilidades.limpiar_consola()
    utilidades.logo()
    utilidades.detector_de_sistema()
    
    print("Tu dirección IP actual es: {}\n".format(public))
    print("[1] Informacion de una direccion IP")
    print("[2] Escaneo de un servidor web")
    print("[3] Instalar un paquete PiP")
    print("[4] IP Grabber [WZ, RL, Minecraft, Halo y p2p]")

    opc = input("\n¿Qué deseas hacer? ==>  ")
    if opc == '1':
        ip = input("Introduce una direccion IP ==> ")
        localizacion = geo.geolocalizacion(ip)
    elif opc == '2':
        sitio =  input("Inserta el sitio web a escanear :D =>  ")
        sitiosscan.escaneo(sitio)
    elif opc == '3':
        modulo = input("¿Qué modulo quieres instalar? =>  ")
        pipinstaller.instalador.instaladorpip(modulo)
    elif opc == '4':
        wzg.parses()
    else:
        print("No seleccionaste una entrada valida")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario [KeyboardInterrupt]")