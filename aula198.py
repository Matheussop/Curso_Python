# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Matheus', 'Luiz')
# p1.nome = 'Matheus'
# p1.sobrenome = 'Luiz'

p2 = Pessoa('Samuel', 'Luiz')
# p2.nome = 'Samuel'
# p2.sobrenome = 'Luiz'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)