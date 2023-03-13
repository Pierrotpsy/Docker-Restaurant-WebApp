from flask import Flask, request, render_template, redirect
import requests
import json

app = Flask(__name__)

api_url = 'http://backend:5000/restaurants'


@app.route('/')
def index():
    r = requests.get(api_url)
    restaurants = json.loads(r.text)['restaurants']
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
        r = requests.put(api_url + '/' + id, json=data)
        return redirect('/')
    else:
        r = requests.get(api_url + '/' + id)
        restaurant = json.loads(r.text)
        return render_template('edit.html', restaurant=restaurant)


@app.route('/delete/<id>')
def delete(id):
    r = requests.delete(api_url + '/' + id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
