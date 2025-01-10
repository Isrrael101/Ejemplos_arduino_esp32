# Tutorial: Exploración del ESP32 desde Terminal VSCode

## 1. Preparación del Entorno

### Instalar Herramientas Necesarias
Abre el terminal en VSCode (Ctrl + Shift + ñ) y ejecuta:
```bash
pip install esptool  # Para flashear el ESP32
pip install rshell   # Para interactuar con MicroPython
```

### Verificar Instalación
```bash
esptool.py version
rshell --version
```

## 2. Conectar al ESP32

### Identificar Puerto
- Windows: `COM1`, `COM2`, etc. (ver en Administrador de dispositivos)
- Linux: `/dev/ttyUSB0` o similar
- Mac: `/dev/cu.SLAB_USBtoUART`

### Conectar usando rshell
```bash
# Windows
rshell -p COM5 -b 115200

# Linux
rshell -p /dev/ttyUSB0 -b 115200

# Mac
rshell -p /dev/cu.SLAB_USBtoUART -b 115200
```

## 3. Comandos Básicos en rshell

### Navegación y Exploración
```bash
help          # Ver todos los comandos disponibles
boards        # Mostrar dispositivos conectados
ls            # Listar archivos en directorio actual
ls /pyboard   # Listar archivos en ESP32
cd /pyboard   # Cambiar al directorio del ESP32
```

### Manejo de Archivos
```bash
cp archivo.py /pyboard/  # Copiar archivo al ESP32
rm /pyboard/archivo.py   # Borrar archivo del ESP32
cat /pyboard/main.py     # Ver contenido de un archivo
```

## 4. Usar el REPL

### Entrar al REPL
```bash
repl          # Entrar al REPL de MicroPython
```

### Comandos Útiles en REPL
```python
# Información del Sistema
import sys
print(sys.implementation)
print(sys.platform)

# Ver Módulos Disponibles
help('modules')

# Información de Memoria
import gc
print(gc.mem_free())  # Memoria libre
gc.collect()         # Limpiar memoria
```

### Ejemplos Prácticos

#### Control de LED
```python
from machine import Pin
import time

# Configurar LED
led = Pin(2, Pin.OUT)

# Encender/Apagar
led.value(1)    # Encender
led.value(0)    # Apagar

# Parpadeo
for i in range(5):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
```

#### Lectura ADC
```python
from machine import ADC, Pin

# Configurar ADC
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

# Leer valores
valor = adc.read()
print(valor)

# Lectura continua
import time
while True:
    print(adc.read())
    time.sleep(0.5)
```

## 5. Atajos y Comandos Especiales

### En rshell
- `Ctrl + D`: Salir del REPL
- `Ctrl + X`: Salir de rshell
- `Ctrl + C`: Interrumpir operación actual

### En REPL
- `Ctrl + C`: Interrumpir programa
- `Ctrl + D`: Soft reset
- `Ctrl + E`: Entrar en modo pegado
- `Ctrl + A`: Ir al inicio de la línea
- `Ctrl + E`: Ir al final de la línea

## 6. Solución de Problemas

### Error de Conexión
Si no puedes conectar:
1. Verifica el puerto correcto
2. Desconecta y reconecta el ESP32
3. Cierra y vuelve a abrir VSCode
4. Intenta con una velocidad diferente (e.g., `-b 9600`)

### REPL No Responde
1. Presiona `Ctrl + C` varias veces
2. Si no funciona, `Ctrl + D` para reset
3. Si aún no responde, desconecta y reconecta el ESP32

### Errores de Permiso (Linux/Mac)
```bash
sudo chmod 666 /dev/ttyUSB0  # Linux
sudo chmod 666 /dev/cu.SLAB_USBtoUART  # Mac
```

## 7. Tips Adicionales

### Guardar Configuración
Crea un archivo `.rshell` en tu directorio home:
```
PYBOARD_DEVICE = '/dev/ttyUSB0'
EDITOR = 'code'
```

### Automatizar Tareas
Crea scripts de Python y ejecútalos:
```bash
rshell -p COM5 cp script.py /pyboard/main.py
```
