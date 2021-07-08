try:
    from modulos.reverse import sitiosscan
    from modulos.geo import geo
    from modulos.selfip import ip
    import modulos.utilidades as utilidades
    import modulos.pipinstaller as pipinstaller
except:
    print("Uno o más modulos necesitan descargarse, comprueba el git o contacta a Mitnez.")

public = ip.ippublica()

def main():
    utilidades.limpiar_consola()
    utilidades.logo()
    
    print("Tu dirección IP actual es: {}\n".format(public))
    print("[1] Informacion de una direccion IP")
    print("[2] Escaneo de un servidor web")
    print("[3] Instalar un paquete PiP")

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
    else:
        print("No seleccionaste una entrada valida")
try:
    main()
except:
    pass