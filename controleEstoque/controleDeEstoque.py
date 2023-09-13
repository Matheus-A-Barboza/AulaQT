import sqlite3
import sys
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QTableWidget, QAbstractItemView, \
    QPushButton, QLineEdit, QLabel, QWidget, QMessageBox


class Estoque(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Controle de Estoque')
        self.setGeometry(100, 100, 800, 400)

        self.conn = sqlite3.connect('estoque.db')
        self.cursor = self.conn.cursor()

        self.criar_tabela()

        layout_principal = QHBoxLayout()
        layout_esquerda = QVBoxLayout()
        layout_direita = QVBoxLayout()
        layout_botoes = QHBoxLayout()

        self.tbl_produtos = QTableWidget()
        self.tbl_produtos.verticalHeader().setVisible(False)
        self.tbl_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)

        layout_direita.addWidget(self.tbl_produtos)

        self.btn_cadastar = QPushButton('Cadastrar')
        self.btn_remover = QPushButton('Remover')
        self.btn_editar = QPushButton('Editar')
        self.btn_limpar = QPushButton('Limpar Campos')

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
        # layout_esquerda.addWidget(self.btn_limpar_banco)
        layout_esquerda.addWidget(self.btn_limpar)
        layout_esquerda.addLayout(layout_botoes)

        layout_principal.addLayout(layout_esquerda)
        layout_principal.addLayout(layout_direita)

        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)

        self.btn_cadastar.clicked.connect(self.inserir_produtos)
        self.btn_limpar.clicked.connect(self.limpar_campos)

    def criar_tabela(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL TEXT NOT NULL,
                quantidade INT NOT NULL,
                data_validade TEXT,
                categoria TEXT NOT NULL,
                fornecedor TEXT NOT NULL
                )''')
            self.conn.commit()
        except Exception as e:
            print(e)

    def inserir_produtos(self):
        if self.validar_data():
            try:
                self.cursor.execute(
                    "INSERT INTO produtos (nome, preco,"
                    "quantidade, data_validade, categoria,"
                    "fornecedor) VALUES (?, ?, ?, ?, ?, ?)", (self.txt_nome.text(),
                                                              self.txt_preco.text(),
                                                              self.txt_qnt.text(),
                                                              self.txt_data.text(),
                                                              self.txt_categoria.text(),
                                                              self.txt_fornecedor.text()))
                self.conn.commit()
                QMessageBox.information(self, 'Cadastro de Produto', 'Produto Adicionado com Sucesso')
                self.limpar_campos()

            except Exception as e:
                print(e)

    # def limpar_banco(self):
    #     try:
    #         self.cursor.execute(
    #             "TRUNCATE TABLE produtos"
    #         )
    #         self.conn.commit()
    #     except Exception as e:
    #         print(e)

    def limpar_campos(self):
        self.txt_nome.clear()
        self.txt_preco.clear()
        self.txt_qnt.clear()
        self.txt_data.clear()
        self.txt_categoria.clear()
        self.txt_fornecedor.clear()

    def validar_data(self):
        try:
            datetime.strptime(self.txt_data.text(), '%d,%m,%Y')
            return True
        except:
            QMessageBox.warning(self, 'Aviso', 'Data de Validade fora do padrão dd/mm/aaaa')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Estoque()
    window.show()
    sys.exit(app.exec())
