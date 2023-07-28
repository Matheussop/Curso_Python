# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'daniel', 'sobrenome': 'Silva'},
    {'nome': 'eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        for keys in item:
            item[keys] = item[keys].capitalize()
        # (key1, _), (key2,_) = item.items()
        # item[key1] = item[key1].capitalize()
        # item[key2] = item[key2].capitalize()
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'].lower())
l2 = sorted(lista, key=lambda item: item['sobrenome'].lower())

exibir(l1)
exibir(l2)