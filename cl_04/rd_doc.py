import csv

caminho_arquivo = 'doc.csv'

dados = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        dados.append(linha)

for registro in dados:
    print(registro)