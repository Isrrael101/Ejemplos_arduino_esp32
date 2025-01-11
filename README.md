# Guía para usar rshell con ESP32 en Windows

## 1. Verificar entorno
```powershell
# Activar entorno virtual
.\entorno\Scripts\activate

# Verificar versión de Python
python --version
# Debería mostrar: Python 3.9.13
```

## 2. Verificar instalación de rshell
```powershell
# Instalar si no está instalado
pip install rshell

# Verificar instalación
rshell --version
```

## 3. Conectar al ESP32
```powershell
# Reemplaza COM5 con tu puerto
rshell -p COM5 --buffer-size 32
```

## 4. Comandos dentro de rshell

### Ver archivos en ESP32:
```bash
ls /pyboard
```

### Copiar archivos al ESP32:
```bash
cp boot.py /pyboard/
cp main.py /pyboard/
```

### Entrar al REPL:
```bash
repl
```

### Comandos útiles REPL:
- Ctrl+C: Interrumpir programa
- Ctrl+D: Soft reset
- Ctrl+X: Salir del REPL
- Ctrl+E: Entrar en modo pegado

### Salir de rshell:
```bash
exit
```

## 5. Script de automatización
Crear archivo `deploy.ps1`:
```powershell
# Contenido de deploy.ps1
$PORT = "COM5"  # Cambia al puerto que uses

Write-Host "Copiando archivos al ESP32..."
rshell -p $PORT --buffer-size 32 "cp boot.py /pyboard/; cp main.py /pyboard/"

Write-Host "Archivos copiados. Iniciando REPL..."
rshell -p $PORT --buffer-size 32 repl
```

## 6. Ejemplo completo de uso
```powershell
# 1. Activar entorno virtual
.\entorno\Scripts\activate
# en gitbash
source .\entorno\Scripts\activate
# 2. Verificar conexión
rshell -p COM5 --buffer-size 32 ls /pyboard

# 3. Copiar archivos
rshell -p COM5 --buffer-size 32 "cp boot.py /pyboard/; cp main.py /pyboard/"

# 4. Verificar archivos copiados
rshell -p COM5 --buffer-size 32 ls /pyboard

# 5. Entrar al REPL
rshell -p COM5 --buffer-size 32 repl
```

## 7. Solución de problemas comunes

### Error "Could not enter raw repl":
1. Desconecta y reconecta el ESP32
2. Espera unos segundos
3. Intenta nuevamente

### Error "Port is busy":
1. Cierra todas las conexiones al puerto
2. Cierra VSCode
3. Desconecta y reconecta el ESP32

### Error "Permission denied":
1. Ejecuta PowerShell como administrador
2. Verifica que el puerto COM es correcto

## 8. Tips adicionales

### Ver contenido de un archivo en ESP32:
```bash
cat /pyboard/main.py
```

### Eliminar archivo del ESP32:
```bash
rm /pyboard/main.py
```

### Crear directorio:
```bash
mkdir /pyboard/lib
```

### Verificar memoria libre:
```python
# En el REPL:
import gc
gc.mem_free()
```

### Reiniciar ESP32:
```python
# En el REPL:
import machine
machine.reset()
```
