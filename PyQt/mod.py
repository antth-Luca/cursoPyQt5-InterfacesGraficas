import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui


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


       self.label2 = QLabel(self)


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
   def config_imagem(nome_label, nome_imagem, largural=450, altural=200, esquerdal=60, topol=300):
       nome_label.move(esquerdal, topol)
       nome_label.setPixmap(QtGui.QPixmap(nome_imagem))
       nome_label.resize(largural, altural)


   @staticmethod
   def config_botao(nome, esquerdab=150, topob=150, largurab=150, alturab=80, cor='#ddeff0', fonte='bold', tamanho='20'):
       nome.move(esquerdab, topob)
       nome.resize(largurab, alturab)
       config = '{' + ('background-color:{};font:{};font-size:{}px'.format(cor, fonte, tamanho)) + '}'
       nome.setStyleSheet(f'QPushButton {config}')


   def acao1(self):
       self.config_label(self.label1, 'Olha o aviãozinho de Capimoney!', '#3b747f')
       self.config_imagem(self.label2, 'Capimoney.jpg', 688, 310)


   def acao2(self):
       self.config_label(self.label1, 'Capi-capibara!', '#e02222')
       self.config_imagem(self.label2, 'Capivara.jpg', 1024, 576, 60, 250)
