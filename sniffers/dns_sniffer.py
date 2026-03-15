import sys
import scapy.all as scapy
import signal

# Función que se ejecuta cuando el usuario presiona CTRL + C (SIGINT)
def def_handler(sig, frame):
    print("Saliendo..\n")
    sys.exit(1)

# Se registra la función anterior como manejador de señales
signal.signal(signal.SIGINT, def_handler)

# Función que procesa cada paquete DNS capturado
def process_dns_packet(packet):
    # Verifica si el paquete contiene una petición DNS (DNS Query)
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()  # Obtiene el dominio que se está consultando y lo decodifica a string

        exclude_keywords =  ["google", "cloud", "bind", "static", "sensic"] # Palabras clave que queremos excluir (consultas comunes o ruidosas)

        # Filtra dominios ya vistos y dominios que incluyan palabras prohibidas
        if domain not in domains_seen and not any(keyword in domain for keyword in exclude_keywords):
            domains_seen.add(domain)
            print(f"[+] Dominio: {domain}")

# Función que inicia el sniffer DNS
def sniff(interface):
    # Filtramos solo paquetes UDP en el puerto 53 (DNS)
    # prn indica qué función ejecutar con cada paquete capturado
    # store=0 evita almacenar los paquetes en memoria
    scapy.sniff(iface=interface, filter='udp and port 53', prn=process_dns_packet, store=0)

# Función principal
def main():
    sniff('ens33')# Inicia el sniffer en la interfaz deseada
    


if __name__ =='__main__':
    global domains_seen
    domains_seen = set() # Estructura para guardar dominios ya procesados
    main()
