import json

pessoa = {
    'nome': 'Matheus Luiz',
    'sobrenome': 'Oliveira',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': ((2, 4),( 7, 9), 11),
    'dev': True,
    'nada': None,
}

with open('aula190.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=4,
    )

with open('aula190.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])