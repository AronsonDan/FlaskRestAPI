from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList
from security import authenticate, identity

# Declare the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qurbppsijzqymd:0c31efb337fbd063538ee7e6585e3abc254f37b71c4fcb9598517ef3576d607a@ec2-54-75-231-85.eu-west-1.compute.amazonaws.com:5432/d70q403p5r0vq7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'

# Declare the API
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
