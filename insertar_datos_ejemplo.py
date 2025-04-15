import sqlite3
from datetime import datetime

conn = sqlite3.connect("envios.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO guias (
    nombre, telefono, ciudad, direccion, direccion_secundaria,
    tipo_id, numero_id, correo, producto, ancho, alto, largo,
    peso, valor_asegurado, contenido, pago, fecha_creacion
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "Carolina Pantoja", "0991234567", "Guayaquil", "Av. Principal 123",
    "Edificio Los Álamos", "Cédula ciudadanía (CC)", "1102938475",
    "carolina@email.com", "Camiseta L", 30.0, 10.0, 20.0, 0.5,
    10000, "Camiseta para regalo", "Crédito", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
))

conn.commit()
conn.close()
print("Ejemplo insertado.")
