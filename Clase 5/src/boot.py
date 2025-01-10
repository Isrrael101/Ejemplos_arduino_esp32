# boot.py
import network
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('Conectado!')
    print('IP:', wlan.ifconfig()[0])

# Configura aquí tu WiFi
connect_wifi('tu_ssid', 'tu_password')