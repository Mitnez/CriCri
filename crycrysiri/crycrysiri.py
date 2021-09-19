try:
    import modulos.utilidades as utilidades
    import modulos.wzgrab2 as wzg
except:
    print("Uno o más modulos necesitan descargarse, comprueba el git o contacta a m1ttt.")


def main():
    utilidades.limpiar_consola()
    utilidades.logo()
    
    print("===================CryCry IP Grabber Standalone Siri===================")
    wzg.parses()
   

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario [KeyboardInterrupt]")