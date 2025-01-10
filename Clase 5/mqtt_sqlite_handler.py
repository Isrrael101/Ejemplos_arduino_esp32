import paho.mqtt.client as mqtt
import sqlite3
import json
from datetime import datetime

# Configuración de la base de datos
def setup_database():
    conn = sqlite3.connect('sensores.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lecturas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  valor INTEGER,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

# Callback cuando se recibe un mensaje
def on_message(client, userdata, msg):
    try:
        # Decodificar el mensaje
        datos = json.loads(msg.payload.decode())
        
        # Guardar en SQLite
        conn = sqlite3.connect('sensores.db')
        c = conn.cursor()
        c.execute('INSERT INTO lecturas (valor, timestamp) VALUES (?, ?)',
                 (datos['valor'], datetime.now().isoformat()))
        conn.commit()
        conn.close()
        
        print(f"Dato guardado: {datos['valor']}")
        
    except Exception as e:
        print("Error:", e)

# Callback cuando nos conectamos
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT")
    client.subscribe("sensor/datos")

def main():
    # Configurar base de datos
    setup_database()
    
    # Configurar cliente MQTT
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Conectar al broker
    print("Conectando al broker MQTT...")
    client.connect("localhost", 1883, 60)
    
    # Mantener el programa corriendo
    client.loop_forever()

if __name__ == "__main__":
    main()