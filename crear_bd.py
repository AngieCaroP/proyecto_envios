import sqlite3

# Conexión y creación de la base de datos
conn = sqlite3.connect('envios.db')
cursor = conn.cursor()

# Tabla de guías generadas
cursor.execute('''
CREATE TABLE IF NOT EXISTS guias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    ciudad TEXT NOT NULL,
    direccion TEXT NOT NULL,
    direccion_secundaria TEXT,
    tipo_id TEXT,
    numero_id TEXT,
    correo TEXT,
    producto TEXT,
    ancho REAL,
    alto REAL,
    largo REAL,
    peso REAL,
    valor_asegurado REAL,
    contenido TEXT,
    forma_pago TEXT,
    estado TEXT,
    transportadora TEXT,
    bodega TEXT,
    creado_por TEXT,
    paquetes INTEGER,
    productos INTEGER,
    total REAL
)
''')

# Tabla de productos en stock
cursor.execute('''
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL
)
''')

conn.commit()
conn.close()

print("Base de datos creada correctamente con las tablas 'guias' y 'stock'.")
