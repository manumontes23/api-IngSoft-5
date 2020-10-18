"""
GET (por defecto) obtener
POST guarda
PUT actualizar
DELETE BORRAR
"""

#SE IMPORTA EL FRAMEWORK, PERO ANTES SE DEBE EJECUTAR pip install flask
from flask import Flask, jsonify
from clientes import clientes

app = Flask(__name__)

#RUTAS

#Ruta de prueba
@app.route('/ping')
def print():
    return 'pong'
#Ruta de prueba

#Ruta que devuelve clientes
@app.route('/clientes')
def getClientes():
    return jsonify({"mensaje":"Lista de clientes","clientes":clientes})

#Ruta que devuelve un cliente por id
@app.route('/clientes/<string:id_cliente>')
def getCliente(id_cliente):
    cliente_encontrado = [cliente for cliente in clientes if cliente['id'] == id_cliente ] 
    if (len(cliente_encontrado) > 0 ):
        return jsonify( {"mensaje":"cliente_encontrado", id_cliente:cliente_encontrado} )
    return jsonify( {"mensaje":"cliente_no_encontrado"} )
    

if __name__ == '__main__':
    app.run(debug=True, port=4000)