# dir, hasattr e getattr em Python
string = 'Matheus'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe os dois parametros')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)