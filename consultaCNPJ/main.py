import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Consulta CNPJ')
        self.setGeometry(100, 100, 600, 500)

        # Componente Interface
        self.lbl_cnpj = QLabel('CNPJ')
        self.txt_cnpj = QLineEdit()
        self.btn_consultar = QPushButton('Consultar CNPJ')
        self.lbl_resultado = QLabel()

        # Componentes preencher respostas de consulta
        self.lbl_empresa = QLabel('Nome da Empresa')
        self.txt_empresa = QLineEdit()
        self.lbl_abertura = QLabel('Data da Abertura')
        self.txt_abertura = QLineEdit()
        self.lbl_situacao = QLabel('Situacao')
        self.txt_situacao = QLineEdit()
        self.lbl_tipo = QLabel('Tipo da Empresa')
        self.txt_tipo = QLineEdit()
        self.lbl_endereco = QLabel('Endereco')
        self.lbl_logradouro = QLabel('Logradouro')
        self.txt_logradouro = QLineEdit()
        self.lbl_numero = QLabel('Numero')
        self.txt_numero = QLineEdit()
        self.lbl_bairro = QLabel('Bairro')
        self.txt_bairro = QLineEdit()
        self.lbl_municipio = QLabel('Municipio')
        self.txt_municipio = QLineEdit()
        self.lbl_estado = QLabel('Estado')
        self.txt_estado = QLineEdit()
        self.lbl_cep = QLabel('CEP')
        self.txt_cep = QLineEdit()
        self.btn_limpar_campos = QPushButton('Limpar Campos')

        # self.btn_limpar_campos.clicked.connect(self.limpar_campos)

        # Criar e inserir campos ao layout

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_cnpj)
        layout.addWidget(self.txt_cnpj)
        layout.addWidget(self.btn_consultar)
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.lbl_empresa)
        layout.addWidget(self.txt_empresa)
        layout.addWidget(self.lbl_abertura)
        layout.addWidget(self.txt_abertura)
        layout.addWidget(self.lbl_situacao)
        layout.addWidget(self.txt_situacao)
        layout.addWidget(self.lbl_tipo)
        layout.addWidget(self.txt_tipo)
        layout.addWidget(self.lbl_endereco)
        layout.addWidget(self.lbl_logradouro)
        layout.addWidget(self.txt_logradouro)
        layout.addWidget(self.lbl_numero)
        layout.addWidget(self.txt_numero)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.txt_bairro)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.txt_bairro)
        layout.addWidget(self.lbl_municipio)
        layout.addWidget(self.txt_municipio)
        layout.addWidget(self.lbl_estado)
        layout.addWidget(self.txt_estado)
        layout.addWidget(self.lbl_cep)
        layout.addWidget(self.txt_cep)
        layout.addWidget(self.btn_limpar_campos)

        self.btn_consultar.clicked.connect(self.consulta_cnpj)

        # Definindo Widget na tela
        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def consulta_cnpj(self):
        cnpj = (self.txt_cnpj.text()
                .replace('-', '')
                .replace('/', '')
                .replace('.', ''))

        if self.valida_cnpj(cnpj):
            dados = self.obter_dados(cnpj)
            if dados:
                self.preenche_dados(dados)
        else:
            self.lbl_resultado.setText('CNPJ Invalido')

    def preenche_dados(self, dados):
        self.txt_empresa.setText(dados.get('nome', ''))
        self.txt_abertura.setText(dados.get('abertura', ''))
        self.txt_situacao.setText(dados.get('situacao', ''))
        self.txt_tipo.setText((dados.get('tipo', '')))
        self.txt_logradouro.setText((dados.get('logradouro', '')))
        self.txt_numero.setText((dados.get('numero', '')))
        self.txt_bairro.setText((dados.get('bairro', '')))
        self.txt_municipio.setText((dados.get('municipio', '')))
        self.txt_estado.setText((dados.get('estado', '')))
        self.txt_cep.setText((dados.get('cep', '')))

    def obter_dados(self, cnpj):
        url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()

        except Exception as e:
            self.lbl_resultado.setText(f'Erro ao Consultar CNPJ. Erro {e}')
            return None

    def valida_cnpj(self, cnpj):
        return cnpj.isnumeric() and len(cnpj) == 14

    def limpar_campos(self):
        self.txt_empresa.setText('')
        self.txt_abertura.setText('')
        self.txt_situacao.setText('')
        self.txt_tipo.setText('')
        self.txt_logradouro.setText('')
        self.txt_numero.setText('')
        self.txt_bairro.setText('')
        self.txt_municipio.setText('')
        self.txt_estado.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
