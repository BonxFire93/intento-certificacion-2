from flask_app.config.mysqlconnection import connectToMySQL

DB_NAME = 'viajero frecuente'

class Destino:
    def __init__(self, data):
        self.id = data.get('id')
        self.destino = data.get('destino')
        self.inicio = data.get('inicio')
        self.fin = data.get('fin')
        self.itinerario = data.get('itinerario')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.nombre_org = data.get('nombre_org')
        self.apellido_org = data.get('apellido_org')

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO destinos (destino, inicio, fin, itinerario, created_at, updated_at) VALUES ( %(destino)s, %(inicio)s, %(fin)s, %(itinerario)s, NOW(), NOW())'
        return connectToMySQL('viajero frecuente').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM destinos'
        destinos_en_db = connectToMySQL('viajero frecuente').query_db(query)
        destinos = []
        for destino in destinos_en_db:
            destinos.append(cls(destino))
        return destinos

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM destinos WHERE id = %(id)s;'
        destino_en_db = connectToMySQL('viajero frecuente').query_db(query, data)
        if not destino_en_db:
            return None
        return cls(destino_en_db[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATED destinos SET destino=%(destino)s, inicio=%(inicio)s, fin=%(fin)s, itinerario=%(itinerario)s, created_at=NOW(), updated_at=NOW() WHERE id=%(id)s;'
        return connectToMySQL('viajero frecuente').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM destinos WHERE id=%(id)s;'
        return connectToMySQL('viajero frecuente').query_db(query, data)