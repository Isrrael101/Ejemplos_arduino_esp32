from machine import ADC, Pin
from time import sleep_ms

# Configurar el ADC
# GPIO36 (Pin 36) corresponde a ADC1_CH0
adc = ADC(Pin(36))

# Configurar el rango de voltaje del ADC (0-3.3V)
adc.atten(ADC.ATTN_11DB)    # Rango completo: 3.3v

# Configurar la resolución a 12 bits (0-4095)
adc.width(ADC.WIDTH_12BIT)

while True:
    # Leer el valor analógico
    valor = adc.read()
    
    # Imprimir el valor
    print(valor)
    
    # Esperar 100ms
    sleep_ms(100)