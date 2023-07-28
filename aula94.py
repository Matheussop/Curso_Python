"""
Lista de listas e seus índices
"""
salas = [ ['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda'] ]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)