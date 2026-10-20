from flask_app import app
from flask import render_template, session, redirect, request #type:ignore
from flask_app.models.usuario import Usuario
from flask_app.models.destino import Destino

@app.route('/dashboard')
def dashboard():
    print(session['usuario_id'])
    usuario_en_db = Usuario.get_one({'id' : session['usuario_id']})
    destinos = Destino.get_all()
    return render_template('dashboard.html', usuario=usuario_en_db, destinos=destinos)

@app.route('/editar/<int:id>')
def editar(id):
    return render_template('editar.html', id = id)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    Destino.delete({'id':id})
    return redirect('/dashboard')

@app.route('/nuevo')
def nuevo():
    usuarion_sesion = Usuario.get_one('usuario_id')

    return render_template('nuevo.html',usuarion_sesion=usuarion_sesion)

@app.route('/crear_destino', methods = ['POST'])
def crear_destino():
    datos_destino_registro = {
        'destino': request.form['destino'],
        'inicio': request.form['inicio'],
        'fin': request.form['fin'],
        'itinerario': request.form['itinerario']
    }
    nuevo_id = Destino.save(datos_destino_registro)
    session['destino_id'] = nuevo_id
    return redirect('/dashboard')

@app.route('/ver/<int:id>')
def ver(id):
    destino_en_db = Destino.get_one({'id' : id})
    return render_template('ver.html', destino = destino_en_db)