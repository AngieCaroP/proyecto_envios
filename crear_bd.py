import sqlite3

conn = sqlite3.connect("envios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS guias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    telefono TEXT,
    ciudad TEXT,
    direccion TEXT,
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
    pago TEXT,
    fecha_creacion TEXT
)
""")

conn.commit()
conn.close()
print("Base de datos y tabla 'guias' creadas.")
