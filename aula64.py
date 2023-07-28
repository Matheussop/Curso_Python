"""
Iterando strings com while
"""
#       012345678910
# nome = 'Matheus Luiz'  # Iteráveis
#      1110987654321


nome = 'Samuel Luiz'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)