from flask import Flask
import pandas as pd
import os

app = Flask(__name__)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))

@app.route('/')
def home():
    return 'Black Friday 2023 server está rodando'

@app.route('/getData')
def get_data():
    return pd.read_csv(os.path.join(root_dir,'datasets/dados_coletados.csv'),index_col=False).to_json(orient='records')

if __name__ == '__main__':
    app.run(port=4000,debug=True)