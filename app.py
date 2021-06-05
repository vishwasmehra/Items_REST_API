
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import jwt, jwt_required


app = Flask(__name__)
api = Api(app)

items = [

]

class Item(Resource):
    @jwt_required
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return{'name': name, 'price': item['price']}, 200
        return{'message': 'Item not found'}, 404

    def post(self, name):
        for item in items:
            if item['name'] == name:
                return{'message': 'Item already exists'}, 400
            
        data = request.get_json()
        item = {'name': name, 'price':data['price']}
        items.append(item)
        return item, 200



    def put(self, name):
        pass

    def delete(self, name):
        pass

class Items(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port= 5000)