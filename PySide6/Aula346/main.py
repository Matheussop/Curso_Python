import sys

from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from display import Display
from info import Info
from buttons import Button, ButtonsGrid


def temp_label(texto):
    label = QLabel(texto)
    label.setStyleSheet('font-size: 150px;')
    return label


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    setupTheme()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    display.setPlaceholderText('Teste')

    # # Button
    # button = Button('Texto do botão')
    # window.addWidgetToVLayout(button)

    # button2 = Button('Texto do botão')
    # window.addWidgetToVLayout(button2)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
