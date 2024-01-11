"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,People,Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def people():
    people_list = People.query.all() 
    response_body = [people.serialize() for people in people_list]

    return jsonify(response_body), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_unique_people(people_id):
    people_list = People.query.filter_by(id=people_id) 
    response_body = [people.serialize() for people in people_list]

    return jsonify(response_body), 200


@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planets.query.all() 
    response_body = [planets.serialize() for planets in planets_list]

    return jsonify(response_body), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_unique_planets(planets_id):
    people_list = Planets.query.filter_by(id=planets_id) 
    response_body = [planets.serialize() for planets in planets_list]

    return jsonify(response_body), 200    



@app.route('/add_planet', methods=['POST'])
def add_planet():
    new_planet_data = request.json  
    response_body = {
        "msg": "planeta agregado"
    }
    return jsonify(response_body), 201          

@app.route('/add_planet', methods=['GET'])
def favorite_planet():
    add_planet = Planets.query.all() 
    response_body = [planets.serialize() for planets in add_planet]

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
