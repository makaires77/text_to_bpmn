# app.py
import json
from flask import Flask, render_template, request
from compare_paradigms import compare_execution_time, update_big_o_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_execution_time', methods=['POST'])
def compare_execution():
    number = int(request.form['number'])  # Obtém o valor de 'n' a partir do formulário
    data = compare_execution_time(number)  # Passa o valor de 'n' como parâmetro
    data_json = json.dumps(data)  # Converte os dados em uma string JSON
    return data_json  # Retorna a string JSON

@app.route('/update_big_o_plot', methods=['POST'])
def update_big_o():
    number = int(request.form['number'])  # Obtém o valor de 'n' a partir do formulário
    data = update_big_o_plot(number)  # Passa o valor de 'n' como parâmetro
    data_bigo_json = json.dumps(data)  # Converte os dados em uma string JSON
    return data_bigo_json  # Retorna a string JSON

# if __name__ == '__main__':
#     app.run(debug=True)
