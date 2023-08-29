import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Consulta CNPJ')
        self.setGeometry(100, 100, 600, 500)

        #Componente Interface
        self.lbl_cnpj = QLabel('CNPJ')
        self.txt_cnpj = QLineEdit()
        self.btn_consultar = QPushButton()

        #Componentes preencher respostas de consulta
        self.lbl_empresa = QLabel('Nome da Empresa')
        self.txt_empresa = QLineEdit()
        self.lbl_abertura = QLabel('Data da Abertura')
        self.txt_abertura = QLineEdit()
        self.lbl_tipo = QLabel('Tipo da Empresa')
        self.txt_tipo = QLineEdit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())