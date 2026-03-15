# Python Cybersecurity Tools

Repositorio con herramientas básicas de ciberseguridad desarrolladas en Python para laboratorios de pentesting y aprendizaje de seguridad ofensiva.

Los scripts incluidos permiten realizar tareas de reconocimiento, enumeración y manipulación de red en entornos controlados.

⚠️ Estas herramientas fueron desarrolladas únicamente con fines educativos y para su uso en laboratorios de seguridad.

---

## Herramientas incluidas

### ARP Scanner
Descubre dispositivos activos en una red local mediante solicitudes ARP.

Funciones:
- Identificación de hosts en la red
- Enumeración de direcciones IP y MAC

---

### ARP Spoof
Implementación de ataque ARP Spoofing para simular ataques Man-in-the-Middle en laboratorio.

Funciones:
- Manipulación de tablas ARP
- Intercepción de tráfico en red local

---

### DNS Sniffer
Captura y analiza consultas DNS en la red.

Funciones:
- Monitorización de tráfico DNS
- Identificación de dominios solicitados

---

### Port Scanner
Escáner de puertos TCP para identificar servicios abiertos en un host objetivo.

Funciones:
- Enumeración de puertos abiertos
- Reconocimiento de servicios

---

### ICMP Scanner
Escaneo de red mediante paquetes ICMP para detectar hosts activos.

Funciones:
- Descubrimiento de dispositivos en red
- Identificación de hosts activos

---

### MAC Changer
Script para modificar la dirección MAC de una interfaz de red.

Funciones:
- Cambio dinámico de MAC address
- Anonimización en pruebas de red

---

## Requisitos

Python 3

Librerías:

```bash
pip install scapy
