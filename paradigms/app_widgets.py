from flask import Flask, render_template, request
from compare_paradigms import compare_execution_time, update_big_o_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_execution_time', methods=['POST'])
def run_compare_execution_time():
    compare_execution_time()
    return "Success"

@app.route('/update_big_o_plot', methods=['POST'])
def run_update_big_o_plot():
    curves = request.form.getlist('curves')
    update_big_o_plot(curves)
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)
