# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 32px;')
botao.show()  # Adiciona o widget na hierarquia e exibe a janela

app.exec()  # O loop da aplicação
