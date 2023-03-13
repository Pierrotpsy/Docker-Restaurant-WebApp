from flask import Flask, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:admin123@db:27017'  # Replace with your own URI
api = Api(app)
client = MongoClient(app.config['MONGO_URI'])
db = client['test']
collection = db['restaurants']


class RestaurantList(Resource):
    def get(self):
        restaurants = collection.find()
        restaurants = [restaurant for restaurant in restaurants]
        for restaurant in restaurants:
            restaurant['_id'] = str(restaurant['_id'])
        restaurants = restaurants[0]
        return jsonify({'restaurants': restaurants})


api.add_resource(RestaurantList, '/restaurants')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
