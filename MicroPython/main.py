import network
import socket
import time
import json

#Author: Cervantes Juan
#Punto de Acesso que funcionara como API
def iniciar_punto_acceso():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='ESP8266_AP', password='12345'
    print('Punto de acceso iniciado, nombre de la red: ESP8266_AP')
    print('IP:', ap.ifconfig()[0])

# Crear servidor y manejar las peticiones
def iniciar_servidor():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Servidor en ejecución en http://{}'.format(addr))

    while True:
        cl, addr = s.accept()
        print('Cliente conectado desde', addr)

        # Leer la solicitud del cliente
        request = cl.recv(1024)
        print("Solicitud del cliente:", request)

        # Datos de prueba no quiere decir que sea el final
        datos = {
            "temperatura": 23,
            "humedad": 50
        }

        # Encabezado CORS
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Access-Control-Allow-Origin: *\r\n')  #CUALQUIER ORIGEN
        cl.send('Content-Type: application/json\r\n')
        cl.send('\r\n')
        cl.send(json.dumps(datos))  #DATOS COMO JSON

        #CONEXION CERRADA
        cl.close()

#Punto de acceso
iniciar_punto_acceso()
iniciar_servidor()

