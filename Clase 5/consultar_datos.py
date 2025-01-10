# consultar_datos.py
import sqlite3
from datetime import datetime, timedelta

def ver_ultimos_datos(limite=10):
    conn = sqlite3.connect('sensores.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM lecturas 
                 ORDER BY timestamp DESC 
                 LIMIT ?''', (limite,))
    
    datos = c.fetchall()
    conn.close()
    
    print(f"\nÚltimos {limite} registros:")
    for dato in datos:
        print(f"ID: {dato[0]}, Valor: {dato[1]}, Tiempo: {dato[2]}")

def promedio_ultima_hora():
    conn = sqlite3.connect('sensores.db')
    c = conn.cursor()
    
    una_hora_atras = (datetime.now() - timedelta(hours=1)).isoformat()
    
    c.execute('''SELECT AVG(valor) FROM lecturas 
                 WHERE timestamp > ?''', (una_hora_atras,))
    
    promedio = c.fetchone()[0]
    conn.close()
    
    if promedio:
        print(f"\nPromedio última hora: {promedio:.2f}")

if __name__ == "__main__":
    ver_ultimos_datos()
    promedio_ultima_hora()