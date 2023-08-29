import sys

import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Config de Janela
        self.setWindowTitle('Consulta de CEP')
        self.setGeometry(100,100,500,250)

        #Config da Label e TextBox da entrada
        self.lbl_cep = QLabel('Digite o CEP para Consulta: ')
        self.txt_cep = QLineEdit()
        self.btn_consultar = QPushButton('Consultar')
        self.btn_limpar = QPushButton('Limpar consulta')

        self.lbl_logradouro = QLabel('')
        self.lbl_bairro = QLabel('')
        self.lbl_localidade = QLabel('')
        self.lbl_uf = QLabel('')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.layout.addWidget(self.lbl_cep, 0, 0)
        self.layout.addWidget(self.txt_cep, 0, 1)
        self.layout.addWidget(self.btn_consultar, 0, 2)
        self.layout.addWidget(self.btn_limpar, 0, 3)
        self.layout.addWidget(self.lbl_logradouro, 1, 0)
        self.layout.addWidget(self.lbl_bairro, 2, 0)
        self.layout.addWidget(self.lbl_localidade, 3, 0)
        self.layout.addWidget(self.lbl_uf, 4, 0)

        self.btn_consultar.clicked.connect(self.consulta_cep)
        self.btn_limpar.clicked.connect(self.limpar_campos)

    def consulta_cep(self):

        cep = self.txt_cep
        cep = self.txt_cep.text().replace('-','').replace('.','')
        if cep.isnumeric() and len(cep) == 8:
            url = f'https://viacep.com.br/ws/{cep}/json'
            response = requests.get(url)

            if response.status_code == 200:
                self.popula_campos(response.json())
            else:
                self.lbl_logradouro.setText('CEP Invalido')
        else:
            self.lbl_logradouro.setText('CEP Invalido')


    def popula_campos(self, response):
        self.lbl_logradouro.setText(f'Logradouro: {response["logradouro"]}')
        self.lbl_bairro.setText(f'bairro: {response["bairro"]}')
        self.lbl_localidade.setText(f'localidade: {response["localidade"]}')
        self.lbl_uf.setText(f'uf: {response["uf"]}')

    def limpar_campos(self):
        self.lbl_logradouro.setText('')
        self.lbl_bairro.setText('')
        self.lbl_localidade.setText('')
        self.lbl_uf.setText('')
        self.txt_cep.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())