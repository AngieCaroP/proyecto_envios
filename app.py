from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Datos simulados (puedes conectar con base de datos real)
guias = {}
despachos = {}
ordenes = {}

@app.route('/')
def home():
    return redirect(url_for('crear_guia'))

@app.route('/crear_guia', methods=['GET', 'POST'])
def crear_guia():
    if request.method == 'POST':
        numero_guia = str(uuid.uuid4())[:8]
        datos_guia = {
            'nombre': request.form['nombre'],
            'telefono': request.form['telefono'],
            'ciudad': request.form['ciudad'],
            'direccion': request.form['direccion'],
            'estado': 'PENDIENTE',
            'transportadora': request.form['transportadora'],
            'valor': request.form['valor'],
        }
        guias[numero_guia] = datos_guia

        # Simulación creación despacho
        numero_despacho = str(uuid.uuid4())[:6]
        if numero_despacho not in despachos:
            despachos[numero_despacho] = {
                'estado': 'CREADA',
                'transportadora': datos_guia['transportadora'],
                'bodega': 'BARRANQUILLA',
                'creado_por': 'Juan Carlos',
                'guias': [numero_guia],
            }
        return redirect(url_for('detalle_despacho', despacho_id=numero_despacho))

    return render_template('crear_guia.html')

@app.route('/despacho/<despacho_id>')
def detalle_despacho(despacho_id):
    despacho = despachos.get(despacho_id)
    if not despacho:
        return "Despacho no encontrado", 404
    return render_template('detalle_despacho.html', despacho_id=despacho_id, despacho=despacho, guias=guias)

@app.route('/ordenes/<despacho_id>')
def ordenes_despacho(despacho_id):
    despacho = despachos.get(despacho_id)
    if not despacho:
        return "Despacho no encontrado", 404
    lista_ordenes = [guias[g] for g in despacho['guias']]
    return render_template('ordenes.html', ordenes=lista_ordenes)

if __name__ == '__main__':
    app.run(debug=True)