from security import authenticate, identity
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required


app = Flask(__name__)
app.secret_key = 'hulugrama'
api = Api(app)

jwt = JWT(app, authenticate, identity)  #/auth enpoint

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x:x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        for item in items:
            if item['name'] == name:
                return{'message': 'Item already exists'}, 400
            
        data = request.get_json()
        item = {'name': name, 'price':data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        data = request.get_json()
        for item in items:
            if item['name'] == name:
                item.update(data)
                return item
            else:
                item1 = {'name': name, 'price': data['price']}
                items.append(item1)
                return item1
        
        return {'message': 'Item does not exist'}, 404

    def delete(self, name):
        pass

class Items(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

if __name__ == '__main__':
    app.run(port= 5000)