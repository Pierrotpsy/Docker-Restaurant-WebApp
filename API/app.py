from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:admin123@db:27017'  # Replace with your own URI
api = Api(app)
client = MongoClient(app.config['MONGO_URI'])
db =  client['test']
restaurants = db['restaurants']


class RestaurantList(Resource):
    def get(self):
        cursor = restaurants.find()
        result = []
        for restaurant in cursor:
            restaurant['_id'] = str(restaurant['_id'])
            result.append(restaurant)
            if len(result) == 1000:
                break
        return jsonify({'restaurants': result})


    def post(self):
        data = request.json
        result = restaurants.insert_one(data)
        return jsonify({'inserted_id': str(result.inserted_id)})


class Restaurant(Resource):
    def get(self, id):
        restaurant = restaurants.find_one({'_id': ObjectId(id)})
        if not restaurant:
            return '', 404
        restaurant['_id'] = str(restaurant['_id'])
        return jsonify(restaurant)

    def put(self, id):
        data = request.json
        result = restaurants.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.modified_count == 0:
            return '', 404
        return '', 204


    def delete(self, id):
        result = restaurants.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return '', 404
        return '', 204


api.add_resource(RestaurantList, '/restaurants')
api.add_resource(Restaurant, '/restaurants/<string:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
