import argparse
import signal
import socket
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

open_sockets=[]

def def_handler(sig, frame):
    print(colored(f"[!] Saliendo del programa...", 'red'))

    for socket in open_sockets:
        socket.close()

signal.signal(signal.SIGINT, def_handler) #Ctrl+C

##host = input(f"\n[+]Ingrese una direccion IP: ")

def get_arguments():
    parser=argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t","--target", dest="target",required=True, help="Victim target to scan (Ex: -t 192.168.0.1)")
    parser.add_argument("-p","--port", dest="port",required= True, help="Port range to scan (Ex: -p 1-100)")
    options =parser.parse_args()       
    return options.target, options.port
        
def create_socket():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)

    open_sockets.append(s)

    return s

#Prueba push
def port_scanner(port,host):

    s= create_socket()

    try:
        s.connect((host,port))
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors='ignore').split('\n')

        if response:
            print(colored(f"\n[+] el puerto {port} esta abierto", 'green'))

            for line in response:
                print(colored(f"{line}",'blue'))
        else:
            print(colored(f"\n[+] El puerto {port} esta abierto",'green'))
                
    except(socket.timeout, ConnectionRefusedError):
        pass

    finally:
        s.close()
    ##print(colored(f"\n[!] El puerto {port} esta cerrado",'red')) 
    
def scan_ports(ports, target):  
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: port_scanner(port, target),ports)
        

def parse_ports(port_str):
    if '-' in port_str:
        start, end =map(int,port_str.split('-'))
        return range (start, end+1)
    elif ',' in port_str:
        return map(int,port_str.split(','))
    else:
        return (int(port_str),)

def main():
    target, port_str = get_arguments()
    ports = parse_ports(port_str)
    scan_ports(ports,target)  
   

if __name__ == '__main__':
    main()
