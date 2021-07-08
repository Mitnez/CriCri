import requests
import modulos.pipinstaller as ip
try:
    from bs4 import BeautifulSoup
except:
    yn = input("Falta el modulo bs4, ¿deseas instalarlo? [y/n]")
    if yn == 'y':
        ip.instalador.instaladorpip(paquete="bs4")
    else:
        print("Instalalo tu, puto")

class sitiosscan():
    def escaneo(*args):
        web = args
        agent = {'User-Agent':'Firefox'}
        try:
            consulta = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(web), headers=agent)
            parse = BeautifulSoup(consulta.text, 'html5lib')
            analizar1 = parse.find(id="null")
            analizar2 = analizar1.find(border="1")
            for i in analizar2.find_all("tr"):
                print("Sitios encontrados: " + i.td.string)
        except:
            print("Hubo un error al tratar de escanear la pagina :(")
            
if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")

