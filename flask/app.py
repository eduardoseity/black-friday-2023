from flask import Flask
from flask import request
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))

def get_df():
    return pd.read_csv(os.path.join(root_dir,'datasets/dados_coletados.csv'),index_col=False)

@app.route('/')
def home():
    return 'Black Friday 2023 server está rodando'

@app.route('/getData')
def get_data():
    return {"dados": list(pd.read_csv(os.path.join(root_dir,'datasets/dados_coletados.csv'),index_col=False).to_dict(orient='records'))}

@app.route('/getSummarizedData')
def get_summarized_data():
    reference = request.args.get('reference')
    df = get_df()
    df = df[df['Referência']==reference]
    date = df['Data'].unique()
    data = []
    for d in date:
        data.append({d: df[df['Data']==d].to_dict(orient='records')})

    return data

@app.route('/getMeanData')
def get_mean_data():
    reference = request.args.get('reference')
    df = get_df()
    df = df[df['Referência']==reference]
    date = df['Data'].unique()
    data = []
    for d in date:
        data.append({d: round(df[df['Data']==d]['Preço'].mean(),2)})

    return data

@app.route('/getMeanAndMedianData')
def get_mean_and_median_data():
    reference = request.args.get('reference')
    df = get_df()
    df = df[df['Referência']==reference]
    date = df['Data'].unique()
    data = []
    for d in date:
        data.append({d: {
                'Média': round(df[df['Data']==d]['Preço'].mean(),2),
                'Mediana': round(df[df['Data']==d]['Preço'].median(),2),
                'Mínimo': round(df[df['Data']==d]['Preço'].min(),2),
                'Máximo': round(df[df['Data']==d]['Preço'].max(),2),
            }})

    return data


if __name__ == '__main__':
    app.run(port=4000,host='0.0.0.0',debug=True)
