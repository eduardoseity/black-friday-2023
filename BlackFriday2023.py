import requests
import json
from datetime import datetime
from fuzzywuzzy import fuzz
import pandas as pd
import os

def coletar_da_url(url: str, palavras_chaves: list) -> tuple:
    # Requisita a url
    req = requests.get(url)
    texto_html = req.text
    # Quebra o texto no ponto da página que possui as informações em formato json
    resultado = texto_html.split('window.__PRELOADED_STATE__ =\n')[-1]
    # Limpa o restante do código que não faz parte do json
    resultado = resultado.split('},props:')[0].replace('};', '}')
    resultado = json.loads(resultado)['initialState']['results']

    # Seleciona apenas os resultados que possuem as palavras chaves no título
    dados_analisados = []
    melhor_ratio = 0
    # Itera entre todos os resultados
    for r in resultado:
        ratio = []
        # Itera entre todas as palavras chaves
        for chave in palavras_chaves:
            # Elimina os espaços e transfoma em minúsculo as duas frases a serem comparadas
            frase1 = r['title'].replace(' ', '').lower()
            frase2 = chave.replace(' ', '').lower()
            # Calcula a porcentagem de proximidade das frases
            ratio.append(fuzz.partial_ratio(frase1, frase2))
        ratio = round(sum(ratio)/len(ratio), 0)
        dados_analisados.append((ratio, r))
        # Grava o recorde do ratio de proximidade
        if melhor_ratio < ratio:
            melhor_ratio = ratio

    # Monta uma lista com os resultados que obtiveram o maior ratio
    dados_selecionados = [x[1] for x in dados_analisados if x[0] == melhor_ratio]

    # Adiciona a data e referência
    data = datetime.today().strftime('%d/%m/%y')
    for i in range(len(dados_selecionados)):
        dados_selecionados[i]['Data'] = data
        dados_selecionados[i]['Referência'] = ' '.join(palavras_chaves)

    # Filtra os dados relevantes
    dados = filtrar(dados_selecionados)

    return dados

def filtrar(items:list) -> dict:
    dados = {
        'Referência': [],
        'Data': [],
        'Título': [],
        'Link': [],
        'id': [],
        'Preço': [],
    }
    for item in items:
        dados['Referência'].append(item['Referência'])
        dados['Data'].append(item['Data'])
        dados['Título'].append(item['title'])
        dados['Link'].append(item['permalink'])
        dados['id'].append(item['id'])
        dados['Preço'].append(item['price']['amount'])
    return dados

if __name__ == '__main__':
    # Abre o dataset
    try:
        df = pd.read_csv('datasets/dados_coletados.csv')
    except FileNotFoundError:
        df = pd.DataFrame()
    
    # Carrega os itens de busca
    with open('busca.json','r') as file:
        busca = json.loads(file.read())
    
    # Transforma os resultados em DataFrame
    dfs = [df]
    for b in busca:
        _df = pd.DataFrame(coletar_da_url(b['url'],b['palavras_chaves']))
        dfs.append(_df)
    
    # Concatena os DataFrames e salva o arquivo
    df = pd.concat(dfs)
    if not os.path.exists('datasets'):
        os.mkdir('datasets')
    df.to_csv('datasets/dados_coletados.csv',index=False)
