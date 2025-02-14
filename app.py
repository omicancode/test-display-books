from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mengizinkan akses API Gateway

# Ganti dengan URL API Gateway Anda
API_GATEWAY_URL = "https://wpgm6vwy8h.execute-api.us-east-1.amazonaws.com/production/books"

@app.route('/')
def index():
    response = requests.get(API_GATEWAY_URL)
    books = response.json() if response.status_code == 200 else []
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    data = {
        "id": request.form['id'],
        "title": request.form['title'],
        "author": request.form['author']
    }
    requests.post(API_GATEWAY_URL, json=data)
    return redirect(url_for('index'))

@app.route('/edit/<id>', methods=['POST'])
def edit_book(id):
    data = {
        "id": id,
        "title": request.form['title'],
        "author": request.form['author']
    }
    requests.put(f"{API_GATEWAY_URL}/{id}", json=data)
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET'])
def delete_book(id):
    requests.delete(f"{API_GATEWAY_URL}/{id}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
