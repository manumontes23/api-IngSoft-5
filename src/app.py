  
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, String, MetaData
from decouple import config as config_decouple

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

@app.route('/bdConnect',methods=['GET'])
def bdConnect():
    return jsonify({'response': 'pong!'})

if __name__ == "__main__":
	app.run()
    