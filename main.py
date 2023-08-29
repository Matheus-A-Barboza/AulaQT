import sys

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QApplication, QLabel, QPushButton


class CalculadoraAreaCubo(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura o titulo da janela
        self.setWindowTitle("Calculadora de Area para Cubos")

        # Cria Widget Principal na Janela
        widget_principal = QWidget()
        # Define posição do Widget
        self.setCentralWidget(widget_principal)

        # Cria layout para Widget Principal
        layout = QVBoxLayout()
        widget_principal.setLayout(layout)

        # Insere Campo para Interação Com Usuario
        self.txt_largura = QLineEdit()
        self.txt_altura = QLineEdit()
        self.txt_comprimento = QLineEdit()

        layout.addWidget(QLabel('Largura'))
        layout.addWidget((self.txt_largura))

        layout.addWidget(QLabel('Altura'))
        layout.addWidget((self.txt_altura))

        layout.addWidget(QLabel('Comprimento'))
        layout.addWidget((self.txt_comprimento))

        # Cria o botao e informa o texto do botao
        self.btn_calcular = QPushButton('Calcular Area')
        layout.addWidget(self.btn_calcular)

        self.lbl_resultado = QLabel('Area do Cubo: ')
        layout.addWidget(self.lbl_resultado)

        self.btn_calcular.clicked.connect(self.calcula_area)

    def calcula_area(self):
        try:
            largura = float(self.txt_largura.text())
        except ValueError:
            self.lbl_resultado.setText('O valor da largura não é válido')

        try:
            altura = float(self.txt_altura.text())
        except ValueError:
            self.lbl_resultado.setText('O valor da altura não é válido')

        try:
            comprimento = float(self.txt_comprimento.text())
        except ValueError:
            self.lbl_resultado.setText('O valor do comprimento não é válido')

        area = largura * altura * comprimento
        self.lbl_resultado.setText(f'A área do Cubo é: {area}')


if __name__ == '__main__':
    # Cria um app QT(QApplication)
    app = QApplication(sys.argv)
    # Cria a instancia da calculadora
    calculadora = CalculadoraAreaCubo()
    # Exibe a tela do app
    calculadora.show()
    # Inicia o loop de eventos da aplicaçãp e espera ate
    # que a janela seja fechada
    sys.exit(app.exec())
