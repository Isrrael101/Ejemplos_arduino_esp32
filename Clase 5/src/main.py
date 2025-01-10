# main.py
from umqtt.simple import MQTTClient
import network
import time
import json
from machine import ADC, Pin

# Configuración
WIFI_SSID = "tu_wifi"
WIFI_PASSWORD = "tu_password"
MQTT_BROKER = "192.168.1.100"  # IP de tu computadora
MQTT_TOPIC = b"sensor/datos"

# Configurar ADC
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)

def conectar_wifi():
    print("Conectando a WiFi...")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wifi.isconnected():
        time.sleep(1)
    print("WiFi conectado:", wifi.ifconfig()[0])

def conectar_mqtt():
    client = MQTTClient("esp32", MQTT_BROKER)
    client.connect()
    print("MQTT conectado")
    return client

def main():
    try:
        # Conectar WiFi
        conectar_wifi()
        
        # Conectar MQTT
        client = conectar_mqtt()
        
        # Bucle principal
        while True:
            # Leer sensor
            valor = adc.read()
            
            # Crear mensaje
            mensaje = json.dumps({
                'valor': valor
            })
            
            # Publicar
            client.publish(MQTT_TOPIC, mensaje)
            print("Dato enviado:", valor)
            
            # Esperar
            time.sleep(5)
            
    except Exception as e:
        print("Error:", e)
        time.sleep(10)
        machine.reset()  # Reiniciar en caso de error

if __name__ == 'main':
    main()