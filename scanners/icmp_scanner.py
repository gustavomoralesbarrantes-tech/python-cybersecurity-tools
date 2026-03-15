import argparse
import subprocess
import signal
import sys
from concurrent.futures import ThreadPoolExecutor

def def_handler(sig, frame):
    print(f"\n[!] Saliendo..")
    sys.exit(1)
    
signal.signal(signal.SIG_IGN, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description= "Herramienta para descubrir host activos en una red")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")
    args = parser.parse_args()

    return args.target

def parse_target(target_str):
    #192.168.1.1-100
    target_str_splitted = target_str.split('.') #["192","168", "1","1-100"]
    frist_three_octets = '.'.join(target_str_splitted[:3])

    if len(target_str_splitted) == 4:
        if "-" in target_str_splitted[3]:
            star, end =target_str_splitted[3].split('-')
            return [f"{frist_three_octets}.{i}" for i in range(int(star), int(end)+1)]
        else:
            return[target_str]
    else:
        print(f"\n[!] El formato ip o rango no es valido")

def host_discovery(target):
    
    try:
        ping=subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
        if ping.returncode == 0:
                print(f"\t[i] La ip {target} esta activa")
    except subprocess.TimeoutExpired:
        pass

def main():
    target_str = get_arguments()
    targets = parse_target(target_str)
    max_threads =100

    print(f"\n[+] Hosts activos en la red:\n")
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discovery,targets)



if __name__ == '__main__':
    main()
