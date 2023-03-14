from flask import Flask, request, render_template, redirect
from datetime import datetime
from pytz import timezone
import requests
import json

app = Flask(__name__, template_folder='templates')

api_url = 'http://backend:5000/restaurants'


def avg_grade(grades):
    total_score = 0
    for grade in grades:
        total_score += grade['score']
    return round(total_score / len(grades), 1)


def timestampformat(timestamp):
    tz = timezone('Europe/Paris')
    dt = datetime.fromtimestamp(timestamp / 1000, tz)
    return dt.strftime('%d/%m/%Y')


app.jinja_env.filters['timestampformat'] = timestampformat


@app.route('/')
def index():
    r = requests.get(api_url)
    restaurants = json.loads(r.text)['restaurants']
    for restaurant in restaurants:
        restaurant['rating'] = avg_grade(restaurant['grades'])

    return render_template('index.html', restaurants=restaurants)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {}
        data['name'] = request.form['name']
        data['cuisine'] = request.form['cuisine']
        data['borough'] = request.form['borough']
        data['address'] = {}
        data['address']['street'] = request.form['street']
        data['address']['building'] = request.form['building']
        data['address']['zipcode'] = request.form['zipcode']
        data['address']['coord'] = [float(request.form['longitude']), float(request.form['latitude'])]
        r = requests.post(api_url, json=data)
        return redirect('/')
    else:
        return render_template('add.html')


@app.route('/restaurant/<id>/details')
def details(id):
    r = requests.get(api_url + '/' + id)
    restaurant = json.loads(r.text)
    restaurant['rating'] = avg_grade(restaurant['grades'])
    return render_template('detail.html', restaurant=restaurant)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        data = {}
        data['name'] = request.form['name']
        data['cuisine'] = request.form['cuisine']
        data['borough'] = request.form['borough']
        data['address'] = {}
        data['address']['street'] = request.form['street']
        data['address']['building'] = request.form['building']
        data['address']['zipcode'] = request.form['zipcode']
        data['address']['coord'] = [float(request.form['longitude']), float(request.form['latitude'])]
        requests.put(api_url + '/' + id, json=data)
        return redirect('/')
    else:
        r = requests.get(api_url + '/' + id)
        restaurant = json.loads(r.text)
        return render_template('edit.html', restaurant=restaurant)


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    r = requests.delete(api_url + '/' + id)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
