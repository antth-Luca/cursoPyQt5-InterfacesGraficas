from PyQt5.QtWidgets import QMainWindow, QPushButton, QToolTip
from abc import ABC, abstractmethod

class MetaBotao(type(QPushButton), type(ABC)):
    pass

class Botao(ABC, metaclass=MetaBotao):
    def criar_botao(self, nome, topob=200, esquerdab=150, alturab=150, largurab=80):
        nome = QPushButton(nome, self.parent)  # Correção feita aqui
        nome.move(esquerdab, topob)
        nome.resize(alturab, largurab)
        nome.setStyleSheet('QPushButton {background-color:#0FB328; font: bold; font-size:20px}')
        nome.clicked.connect(self.acao)

    @abstractmethod
    def acao(self):
        pass


class Janela(QMainWindow, Botao):
    def __init__(self):
        super().__init__()

        self.esquerda = 100
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.nome_janela = 'Minha primeira janela'

        self.parent = self  # Definindo a própria instância como o pai do botão

        self.criar_botao('Botão1')

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.nome_janela)
        self.show()

    def acao(self):
        print('O botão número 1 foi clicado!')
