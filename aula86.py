"""
Exercício
Exiba os índices da lista
0 Matheus
1 Samuel
2 Luiz
"""
lista = ['Matheus', 'Samuel', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))