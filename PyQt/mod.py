import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from abc import ABC, abstractmethod


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.esquerda = 100
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.nome_janela = 'Minha primeira janela'

        botao1 = Botao1()
        botao1.criar_botão()

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.nome_janela)
        self.show()


class Botao(ABC):
    def __init__(self, nome, topo=150, esquerda=200, altura=150, largura=80):
        self.nome = nome
        self.topo = topo
        self.esquerda = esquerda
        self.altura = altura
        self.largura = largura

    def criar_botão(self):
        self.nome = QPushButton(self.nome, self)
        self.nome.move(self.topo, self.esquerda)
        self.nome.resize(self.altura, self.largura)
        self.nome.setStyleSheet('QPushButton {background-color:#0FB328; font: bold; font-size:20px}')
        self.nome.clicked(self.acao)

    @abstractmethod
    def acao(self):
        pass


class Botao1(Botao):
    def __init__(self):
        super().__init__('Botao1')

    def acao(self):
        print('O botão número 1 foi clicado!')
