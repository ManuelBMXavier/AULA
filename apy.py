from flask import Flask
import random

app = Flask(__name__)

piadas = [
    "Sabes qual é a melhor forma de passar o tempo? Comer relógios!",
    "Qual é a fórmula da água benta? H Deus O!",  
    "O que o tijolo falou para o outro? - Há um ciumento entre nós!",
    "Qual é a diferença entre o gato e a coca-cola? - O gato mia e a coca-cola é light!"
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/piada')
def piada():
    return random.choice(piadas)

@app.route('/piadas/<int:id>')
def piadas_id(id):
    if id < 1 or id > len(piadas):
        return "Piada não encontrada", 404
    return piadas[id - 1]

app.run(host='0.0.0.0', port=8084)