import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel


class Janela(QMainWindow, QPushButton):
    def __init__(self):
        super().__init__()

        self.esquerda = 100
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.nome_janela = 'Minha primeira janela'

        botao1 = QPushButton('Botão1', self)
        self.config_botao(botao1)
        botao1.clicked.connect(self.acao1)

        botao2 = QPushButton('Botão2', self)
        self.config_botao(botao2, 500, 150, 150, 80, '#ffc4c4')
        botao2.clicked.connect(self.acao2)

        self.label1 = QLabel(self)
        self.config_label(self.label1, 'Olá, mundo! Clique em algum botão:')

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.nome_janela)
        self.show()

    @staticmethod
    def config_label(nome, texto, cor='000000', fonte='bold', tamanho='25', esquerdal=50, topol=50, largural=460, altural=25):
        nome.setText(texto)
        nome.move(esquerdal, topol)
        nome.resize(largural, altural)
        config = '{' + ('font:{};font-size:{}px;color:{}'.format(fonte, tamanho, cor)) + '}'
        nome.setStyleSheet(f'QLabel {config}')

    @staticmethod
    def config_botao(nome, esquerdab=150, topob=150, largurab=150, alturab=80, cor='#ddeff0', fonte='bold', tamanho='20'):
        nome.move(esquerdab, topob)
        nome.resize(largurab, alturab)
        config = '{' + ('background-color:{};font:{};font-size:{}px'.format(cor, fonte, tamanho)) + '}'
        nome.setStyleSheet(f'QPushButton {config}')

    def acao1(self):
        self.config_label(self.label1, 'O botão 1 foi clicado!', '#3b747f')

    def acao2(self):
        self.config_label(self.label1, 'O botão 2 foi clicado!', '#e02222')
