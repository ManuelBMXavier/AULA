from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

f1_driver = [
    {   
        "id": 1, 
        "name": "Kimi Antonelli", 
        "team": "Mercedes",
        "podiums": 20
    },
    {
        "id": 2, 
        "name": "Max Verstappen",
        "team": "Red Bull",
        "podiums": 15
    },
    {
        "id": 3, 
        "name": "Charles Leclerc",
        "team": "Ferrari",
        "podiums": 10
    }
]
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/driver')
def drivers():
    return jsonify(random.choice(f1_driver))

@app.route('/drivers/<int:id>')
def drivers_id(id):
    for driver in f1_driver:
        if driver['id'] == id:
            return jsonify(driver) 
    return "Driver not found", 404

visitas = 0

@app.route('/visitas')
def show_visitas():
    global visitas
    visitas += 1
    return visitas

app.run(host='0.0.0', port=8084)