from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get('http://backend:5000/restaurants')
    restaurants = response.json()['restaurants']
    return render_template('index.html', restaurants=restaurants)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
