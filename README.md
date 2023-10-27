# Black Friday 2023 🔥
Um projeto para analisar os preços de produtos até o dia da Black Friday

## Introdução
Projeto iniciado em 24 de outubro com o objetivo de monitorar os preços de determinados produtos e verificar o quanto eles caíram até o dia da Black Friday que ocorre no dia 24 de novembro.

## Motivação
Preciso comprar um celular novo e quero aproveitar as promoções 😆

## Qual é o plano? 🤔
O plano é o seguinte:
1. Determinar os produtos que eu quero monitorar
2. Definir quais dados eu preciso obter
3. Escolher uma plataforma de e-commerce
4. Criar um script para obter os dados
5. Instalar esse script em um servidor para coletar os dados todos os dias
6. Transformar os dados em informação de forma gráfica
7. Analisar os resultados
8. Comprar o celular

## 1. Determinar os produtos que eu quero monitorar
Resolvi monitorar três celulares:

- Samsung Galaxy A14
- Xiaomi Pocophone Poco X5 Pro
- iPhone 15 Pro Max

## 2. Definir quais dados eu preciso obter
Data da coleta dos dados, preço, valor do frete

## 3. Escolher uma plataforma de e-commerce
Escolhi o Mercado Livre porque já fiz um script no passado para coletar alguns dados, então posso reutilizar algumas partes do código

## 4. Criar um script para obter os dados
Fiz um [notebook](https://github.com/eduardoseity/black-friday-2023/blob/25adf949d66ce454b93fe4820182dfdc583e39e3/notebooks/BlackFriday_Sketch_2023.ipynb) no Google Colab para testar de forma rápida as funções necessárias para o script.

Com base nos testes desenvolvi o script [BlackFriday2023.py](https://github.com/eduardoseity/black-friday-2023/blob/25adf949d66ce454b93fe4820182dfdc583e39e3/BlackFriday2023.py) para coletar os dados. Este script faz a consulta dos produtos pré selecionados e salva os resultados em um DataFrame do pandas.

`busca.json` contém os produtos a serem pesquisados
```json
[
    {
        "url":"https://url.da.busca",
        "palavras_chaves":["Samsung Galaxy A14","5g","128GB"]
    },
    {
        "url":"https://url.da.busca",
        "palavras_chaves":["Poco X5 Pro","5g","128GB"]
    }
]
```
`url`: faça a busca pelo produto utilizando o campo de busca do site, copie a url e cole neste campo
<br>
`palavras_chaves`: este é um campo que contém as palavras que serão utilizadas para refinar a busca, se faz necessário por conta da variedade de produtos que a busca retorna. Utilizando essas palavras chaves fazemos um filtro para garantir que os resultados sejam mais próximos do produto desejado

`datasets/dados_coletados.csv` contém os resultados obtidos
Este arquivo é gerado automaticamente na primeira vez que o script é executado, a partir daí os resultados são adicionados a esse arquivo.

## 5. Instalar esse script em um servidor para coletar os dados todos os dias
Para rodar o script utilizei um Raspberry Pi 3 rodando o Ubuntu Server 23.04.
<br>Clonei este repositório em uma pasta e configurei a execução diária do script utilizando o `crontab` que é um recurso capaz de executar comandos agendados dentro do sistema.
Este [link](https://guialinux.uniriotec.br/crontab/)<sup>[1]</sup> possui uma explicação sobre o funcionamento deste recurso.

## Tecnologias utilizadas
![Static Badge](https://img.shields.io/badge/python-3.10-blue)
![Static Badge](https://img.shields.io/badge/requests-yellow)
![Static Badge](https://img.shields.io/badge/BeautifulSoup4-purple)
![Static Badge](https://img.shields.io/badge/pandas-brown)

## Referências
[1] https://guialinux.uniriotec.br/crontab/

### Keep in touch
- https://www.github.com/eduardoseity
- https://www.linkedin.com/in/eduardo-seity-iseri-15908224
- eduardoseity@hotmail.com
