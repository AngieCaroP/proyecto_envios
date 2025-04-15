import json
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
from flask import jsonify

app = Flask(__name__)

DATABASE = 'envios.db'
INVENTARIO_PATH = 'data/InventarioCarolina.json'

def get_db():
    db = getattr(app, '_database', None)
    if db is None:
        db = app._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(app, '_database', None)
    if db is not None:
        db.close()

def cargar_inventario():
    try:
        with open(INVENTARIO_PATH, 'r', encoding='utf-8') as f:
            inventario = json.load(f)
        return inventario
    except FileNotFoundError:
        print(f"Error: El archivo {INVENTARIO_PATH} no se encontró.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo {INVENTARIO_PATH} contiene JSON inválido.")
        return {}

@app.route('/')
def index():
    inventario = cargar_inventario()
    productos = [{"id": key, "nombre": item.get("nombre", "Sin nombre"), "precio": item.get("precio")} for key, item in inventario.items()]
    return render_template('index.html', productos=productos)

@app.route('/obtener_producto/<producto_id>')
def obtener_producto(producto_id):
    inventario = cargar_inventario()
    producto = inventario.get(producto_id)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/crear_guia', methods=['POST'])
def crear_guia():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    ciudad = request.form['ciudad']
    direccion = request.form['direccion']
    direccion_secundaria = request.form.get('direccion_secundaria')
    tipo_id = request.form.get('tipo_id')
    numero_id = request.form.get('numero_id')
    correo = request.form.get('correo')
    producto_id = request.form['producto']
    precio_manual = request.form.get('precio_manual')
    cantidad = request.form.get('cantidad_producto_input')
    contenido = request.form.get('contenido')
    pago = request.form.get('pago')
    fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    inventario = cargar_inventario()
    producto_info = inventario.get(producto_id, {})
    nombre_producto = producto_info.get("nombre", "Desconocido")
    precio_producto = precio_manual if precio_manual else producto_info.get("precio", 0)

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO envios (nombre, telefono, ciudad, direccion, direccion_secundaria,
        tipo_id, numero_id, correo, producto_id, nombre_producto, precio, cantidad, contenido, forma_pago, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, telefono, ciudad, direccion, direccion_secundaria,
          tipo_id, numero_id, correo, producto_id, nombre_producto, precio_producto, cantidad, contenido, pago, fecha_creacion))
    db.commit()
    guia_id = cursor.lastrowid
    cursor.execute("SELECT * FROM envios WHERE id = ?", (guia_id,))
    guia = cursor.fetchone()

    # Pasar los datos del formulario a la plantilla detalle.html
    return render_template('detalle.html', guia=guia,
                           nombre=nombre, telefono=telefono, ciudad=ciudad,
                           direccion=direccion, direccion_secundaria=direccion_secundaria,
                           tipo_id=tipo_id, numero_id=numero_id, correo=correo,
                           producto_id=producto_id, nombre_producto=nombre_producto,
                           precio=precio_producto, cantidad=cantidad, contenido=contenido,
                           pago=pago, fecha_creacion=fecha_creacion)

if __name__ == '__main__':
    # init_db()
    app.run(debug=True)