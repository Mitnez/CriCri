import urllib.request
def ippublica():
        server1 = 'http://soporteweb.com'
        consulta =  urllib.request.build_opener()
        consulta.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]
        try:
            url =  consulta.open(server1, timeout=17)
            respuesta =  url.read()
            respuesta =  respuesta.decode('UTF-8')
            return respuesta
        except:
            print("Hubo un error lol")
            
if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")