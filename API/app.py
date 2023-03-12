from flask import Flask
from flask_restful import Api, Resource
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:admin123@db:27017/restaurants'  # Replace with your own URI
api = Api(app)
mongo = PyMongo(app)

class RestaurantList(Resource):
    def get(self):
        restaurants = mongo.db.restaurants.find()
        return {'restaurants': [restaurant for restaurant in restaurants]}

api.add_resource(RestaurantList, '/restaurants')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
