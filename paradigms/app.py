# app.py
from flask import Flask, render_template, request
from compare_paradigms import compare_execution_time, update_big_o_plot
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_execution_time', methods=['POST'])
def compare_execution():
    data = compare_execution_time()  # Obtém os dados
    data_json = json.dumps(data)  # Converte os dados em uma string JSON
    return data_json  # Retorna a string JSON

@app.route('/update_big_o_plot', methods=['POST'])
def update_big_o():
    n = int(request.form['n'])  # Obtém o valor de 'n' a partir do formulário
    data = update_big_o_plot(n)  # Obtém os dados
    data_json = json.dumps(data)  # Converte os dados em uma string JSON
    return data_json  # Retorna a string JSON

