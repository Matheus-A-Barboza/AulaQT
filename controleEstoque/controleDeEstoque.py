import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QTableWidget, QAbstractItemView, \
    QPushButton, QLineEdit, QLabel, QWidget


class Estoque (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Controle de Estoque')
        self.setGeometry(100, 100, 800, 400)

        layout_principal = QHBoxLayout()
        layout_esquerda = QHBoxLayout()
        layout_direita = QHBoxLayout()
        layout_botoes = QVBoxLayout()

        self.tbl_produtos = QTableWidget()
        self.tbl_produtos.verticalHeader().setVisible(False)
        self.tbl_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)

        layout_direita.addWidget(self.tbl_produtos)

        self.btn_cadastar = QPushButton('Cadastrar')
        self.btn_remover = QPushButton('Remover')
        self.btn_editar = QPushButton('Editar')

        layout_botoes.addWidget(self.btn_editar)
        layout_botoes.addWidget(self.btn_remover)

        self.lbl_nome = QLabel('Nome do Produto')
        self.txt_nome = QLineEdit()
        self.lbl_preco = QLabel('Preço do Produto')
        self.txt_preco = QLineEdit()
        self.lbl_qnt = QLabel('Quantidade do Produto')
        self.txt_qnt = QLineEdit()
        self.lbl_data = QLabel('Data de Validade')
        self.txt_data = QLineEdit()
        self.lbl_categoria = QLabel('Categoria do Produto')
        self.txt_categoria = QLineEdit()
        self.lbl_fornecedor = QLabel('Fornecedor')
        self.txt_fornecedor = QLineEdit()

        layout_esquerda.addWidget(self.lbl_nome)
        layout_esquerda.addWidget(self.txt_nome)
        layout_esquerda.addWidget(self.lbl_preco)
        layout_esquerda.addWidget(self.txt_preco)
        layout_esquerda.addWidget(self.lbl_qnt)
        layout_esquerda.addWidget(self.txt_qnt)
        layout_esquerda.addWidget(self.lbl_data)
        layout_esquerda.addWidget(self.txt_data)
        layout_esquerda.addWidget(self.lbl_categoria)
        layout_esquerda.addWidget(self.txt_categoria)
        layout_esquerda.addWidget(self.lbl_fornecedor)
        layout_esquerda.addWidget(self.txt_fornecedor)
        layout_esquerda.addWidget(self.btn_cadastar)
        layout_esquerda.addLayout(layout_botoes)

        layout_principal.addLayout(layout_esquerda)
        layout_principal.addLayout(layout_direita)

        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Estoque()
    window.show()
    sys.exit(app.exec())