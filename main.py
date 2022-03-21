from modulos import loading

print("Importando y comprobando...")
with loading.Spinner():
    try:
        from modulos import geo, selfip, utilidades, wzgrab as wzg, doxxc
    except ImportError:
        print("Uno o más modulos necesitan descargarse, comprueba el git o contacta a m1ttt.")


def main():
    utilidades.limpiar_consola()
    utilidades.logo("CryCry!", "smisome1")
    utilidades.detector_de_sistema()

    print("Tu dirección IP actual es: {}\n".format(selfip.ippublica()))
    print("[1] Informacion de una direccion IP")
    print("[2] IP Grabber [WZ, RL, Minecraft, Halo y p2p] [BETA]")
    print("[3] Doxx CETI")

    opc = input("\n¿Qué deseas hacer? ==>  ")
    if opc == '1':
        localizacion = geo.geolocalizacion()
    if opc == '2':
        wzg.inicio()
    if opc == '3':
        doxxc.main()
    else:
        print("No seleccionaste una entrada valida")


if __name__ == '__main__':
    main()
