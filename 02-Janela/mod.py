import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.esquerda = 100
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.nome_janela = 'Minha primeira janela'
        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.nome_janela)
        self.show()
