try:
    from scapy.all import * 
    import modulos.post as up
except:
    print("Instala scapy")

mi_ip = '192.168.137.131'
ip_activision = '173.199.97.151'

def parseador():
    pkts =  rdpcap('Data\\logs.pcap')
    dic = {}
    for pkt in pkts:
        temp = pkt.sprintf("%IP.dst%")
        dic[temp] = 1

    for a in dic.keys():
        if not a in mi_ip:
            if not a in ip_activision:
                print(a)
    print("===========================================")
    with open("Data\\" + "iplogs" +'.txt', 'w') as f:
        f.write("Estas son las IPs que encontre: ")
        for a in dic.keys():
            if not a in mi_ip:
                if not a in ip_activision:
                    f.write(a + "\n")
    print("IPs guardadas correctamente :D")   
    print("===========================================")
    print("Subiendo archivo a mitdios")
    up.uploader()

   

if __name__ == "__main__":
    print("No puedes ejecutar este modulo directamente :(")