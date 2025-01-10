from machine import Pin
from time import sleep_ms
import sys

# Configurar el LED en el pin 2 (GPIO2)
led = Pin(2, Pin.OUT)

def process_command(command):
    # Eliminar espacios en blanco y convertir a minúsculas
    command = command.strip().lower()
    
    if command == "encender":
        led.value(1)  # Encender LED
        print("LED encendido")
    elif command == "apagar":
        led.value(0)  # Apagar LED
        print("LED apagado")
    else:
        print("Comando no reconocido")

# Buffer para almacenar los caracteres recibidos
input_buffer = ""

# Bucle principal
while True:
    # Verificar si hay datos disponibles en el puerto serial
    if sys.stdin.readable():
        try:
            # Leer un carácter si está disponible
            char = sys.stdin.read(1)
            
            if char == '\n':
                # Procesar el comando cuando se recibe nueva línea
                process_command(input_buffer)
                input_buffer = ""  # Limpiar el buffer
            else:
                # Agregar el carácter al buffer
                input_buffer += char
        except Exception as e:
            print("Error:", e)
    
    # Pequeña pausa para no saturar el CPU
    sleep_ms(10)