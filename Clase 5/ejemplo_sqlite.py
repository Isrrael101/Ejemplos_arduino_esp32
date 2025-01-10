import sqlite3

# Crear una conexión a la base de datos (se creará si no existe)
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Crear una tabla simple
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')

# Insertar algunos datos
usuarios = [
    ('Ana', 25),
    ('Juan', 30),
    ('María', 28)
]

cursor.executemany('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', usuarios)

# Guardar los cambios
conexion.commit()

# Consultar los datos
cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall()

# Mostrar los resultados
for usuario in resultados:
    print(f'ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}')

# Cerrar la conexión
conexion.close()