import sqlite3

conn = sqlite3.connect('envios.db')
cursor = conn.cursor()

# Insertar ejemplo en stock
productos = [
    ("Reloj Skmei 1274", "Reloj digital resistente al agua", 15, 49.99),
    ("Reloj Curren 8442", "Reloj elegante de acero inoxidable", 10, 89.99),
    ("Reloj G-SHOCK GA-2300", "Reloj deportivo, shockproof", 7, 139.50)
]

cursor.executemany("INSERT INTO stock (nombre, descripcion, cantidad, precio_unitario) VALUES (?, ?, ?, ?)", productos)

# Insertar ejemplo de guía
cursor.execute('''
INSERT INTO guias (
    nombre, telefono, ciudad, direccion, direccion_secundaria, tipo_id, numero_id, correo, producto,
    ancho, alto, largo, peso, valor_asegurado, contenido, forma_pago, estado,
    transportadora, bodega, creado_por, paquetes, productos, total
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    "Juan Carlos San", "0987654321", "Guayaquil", "Av. Principal 123", "Edificio Azul", "Cédula ciudadanía (CC)",
    "1234567890", "juan@correo.com", "Reloj Skmei 1274", 10.5, 5.2, 7.8, 0.4, 10000,
    "1 Reloj Skmei", "Crédito", "Despachada", "DOMINA RECAUDO",
    "FULFILLMENT BARRANQUILLA Tempus company", "Juan Carlos San", 2, 1, 260009
))

conn.commit()
conn.close()

print("Datos de ejemplo insertados.")
