from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash #type: ignore

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
DB_NAME = 'viajero frecuente'

class Usuario:
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW())'
        return connectToMySQL('viajero frecuente').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM usuarios'
        usuarios_en_db = connectToMySQL('viajero frecuente').query_db(query)
        usuarios = []
        for usuario in usuarios_en_db:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM usuarios WHERE id = %(id)s;'
        usuario_en_db = connectToMySQL('viajero frecuente').query_db(query, data)
        print('USUARIO EN DB', usuario_en_db)
        if not usuario_en_db:
            return None
        return cls(usuario_en_db[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATE usuarios DET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, password=%(password)s WHERE id=%(id)s;'
        return connectToMySQL('viajero frecuente').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM usuarios WHERE id=%(id)s;'
        return connectToMySQL('viajero frecuente').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM usuarios WHERE email=%(email)s'
        usuario_en_db = connectToMySQL('viajero frecuente').query_db(query, data)
        print('USUARIO IN DB', usuario_en_db)
        if not usuario_en_db:
            return None
        return cls(usuario_en_db[0])

    @staticmethod
    def validar_registro(formulario):
        es_valido = True
        if len(formulario['nombre']) < 2:
            flash('El nombre debe tener al menos 2 caracteres', 'registro')
            es_valido = False
        if len(formulario['apellido']) < 2:
            flash('El apellido debe tener al menos 2 caracteres', 'registro')
            es_valido = False
        if not EMAIL_REGEX.match(formulario['email']):
            flash('El email no tiene un formato válido', 'registro')
            es_valido = False
        elif Usuario.get_by_email({'email':formulario['email']}):
            print(Usuario.get_by_email({'email':formulario['email']}))
            flash('Ya existe una cuenta con ese email', 'registro')
            es_valido = False
        if formulario['password'] != formulario['password_conf']:
            flash('Las contraseñas no coinciden', 'registro')
            es_valido = False
        return es_valido