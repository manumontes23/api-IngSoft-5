  
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, String, MetaData
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@Localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cedula = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50), unique=True)
    apellidos = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    celular = db.Column(db.String(50), unique=True)
    fijo = db.Column(db.String(50), unique=True)
    nit = db.Column(db.String(50), unique=True)
    rut = db.Column(db.String(50), unique=True)
    riesgo = db.Column(db.String(50), unique=True)
    valor = db.Column(db.String(50), unique=True)

    def __init__(self, cedula, nombre, apellidos, email, celular, fijo, nit, rut,riesgo,valor):
        self.cedula = cedula  
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.celular = celular
        self.fijo = fijo
        self.nit = nit
        self.rut = rut
        self.riesgo = riesgo
        self.valor = valor

db.create_all()

class ClientesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cedula', 'nombre', 'apellidos',
                  'email', 'celular', 'fijo', 'nit', 'rut','riesgo','valor')

cliente_schema = ClientesSchema()
clientes_schema = ClientesSchema(many=True)

#RUTAS
######################################
#SANTIAGO JIMENEZ RAIGOSA
######################################

##########
#GET
##########

#Retorna los clientes del VaR
@app.route('/var/nuevoCliente/<string:id_cliente>')
def varVisualizarClientes():
  clientes = Clientes.query.all()
  result = clientes_schema.dump(clientes)
  return jsonify(result)

#Retorna un cliente especifico que tenga el valor en riesgo
@app.route('/tasks/<id>', methods=['GET'])
def varVisualizarClientesId(id):
  cliente = Clientes.query.get(id)
  return cliente_schema.jsonify(cliente)

##########
#POST
##########
#Crea un nuevo cliente para el VaR Asociar un cliente ya existente al var
@app.route('/var/nuevoCliente', methods=['Post'])
def varCrearClientes():

    nuevo_cliente= Clientes(request.json['cedula'],
                            request.json['nombre'],
                            request.json['apellidos'],
                            request.json['email'],
                            request.json['celular'],
                            request.json['fijo'],
                            request.json['nit'],
                            request.json['rut'],
                            'var',
                            request.json['valor'])
    db.session.add(nuevo_cliente)
    db.session.commit()
    return cliente_schema.jsonify(nuevo_cliente)

##########
#PUT
##########

#Actualiza un cliente para el VaR
@app.route('/tasks/<id>', methods=['PUT'])
def varActualizarClientes(id):
  cliente = Clientes.query.get(id)
  cedula = request.json['cedula']
  nombre = request.json['nombre']
  apellidos = request.json['apellidos']
  email = request.json['email']
  celular = request.json['celular']
  fijo = request.json['fijo']
  nit = request.json['nit']
  rut = request.json['rut']
  riesgo = request.json['riesgo']
  valor = request.json['valor']
  cliente.cedula = cedula
  cliente.nombre = nombre
  cliente.apellidos = apellidos
  cliente.email = email
  cliente.celular = celular
  cliente.fijo = fijo
  cliente.nit = nit
  cliente.rut = rut
  cliente.riesgo = riesgo
  cliente.valor = valor
  db.session.commit()

  return cliente_schema.jsonify(cliente)

##########
#DELETE
##########

#Borra un cliente especifico para el VaR
@app.route('/tasks/<id>', methods=['DELETE'])
def varEliminarClientes(id):
  cliente = Clientes.query.get(id)
  db.session.delete(cliente)
  db.session.commit()
  return cliente_schema.jsonify(cliente)


if __name__ == "__main__":
    app.run(debug=True)