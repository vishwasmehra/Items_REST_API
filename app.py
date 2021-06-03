import sqlite3
from flask import Flask, app, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Item(Resource):
    def get(self, name):
        return{'item': name}, 200

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass

class Items(Resource):
    def get(self):
        pass

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port= 5000)