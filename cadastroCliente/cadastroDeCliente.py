import sqlite3
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QListWidget, QInputDialog, QMessageBox


class CadastroCliente(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cadastro de Cliente')
        self.setGeometry(100, 100, 400, 600)

        self.btn_adicionar = QPushButton('Adicionar')
        self.btn_adicionar.setStyleSheet("background-color: lightgreen;"
                                         "border-radius: 5px;"
                                         "border: 2px solid green;")
        self.btn_adicionar.clicked.connect(self.adicionar_cliente)

        self.btn_editar = QPushButton('Editar')
        self.btn_editar.setStyleSheet("background-color: #F1EB9C;"
                                      "border-radius: 5px;"
                                      "border: 2px solid yellow;")
        self.btn_editar.clicked.connect(self.editar_cliente)

        self.btn_remover = QPushButton('Remover')
        self.btn_remover.setStyleSheet("background-color: #FFA8A8;"
                                       "border-radius: 5px;"
                                       "border: 2px solid red;")
        self.btn_remover.clicked.connect(self.remover_cliente)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.lbl_nome = QLabel('Nome: ')
        self.txt_nome = QLineEdit()
        self.lbl_sobrenome = QLabel('Sobrenome: ')
        self.txt_sobrenome = QLineEdit()
        self.lbl_email = QLabel('Email: ')
        self.txt_email = QLineEdit()

        self.btn_salvar = QPushButton('Salvar')
        self.btn_editar = QPushButton('Editar')
        self.btn_remover = QPushButton('Remover')

        self.lst_cliente = QListWidget()
        self.lst_cliente.itemClicked.connect(self.selecionar_cliente)

        self.layout.addWidget(self.lbl_nome)
        self.layout.addWidget(self.txt_nome)
        self.layout.addWidget(self.lbl_sobrenome)
        self.layout.addWidget(self.txt_sobrenome)
        self.layout.addWidget(self.lbl_email)
        self.layout.addWidget(self.txt_email)
        self.layout.addWidget(self.lst_cliente)
        self.layout.addWidget(self.btn_salvar)
        self.layout.addWidget(self.btn_editar)
        self.layout.addWidget(self.btn_remover)

        # Cria o DB
        self.criar_banco()

        #Preenche Lista Clientes
        self.carregar_clientes()

        # Valida Cliente Selecionado
        self.cliente_selecionado = None

        #Acao Botao
        self.btn_salvar.clicked.connect(self.salvar_cliente)
        self.btn_editar.clicked.connect(self.editar_cliente)

    def criar_banco(self):
        conexao = sqlite3.connect('cadastro_cliente.db')
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                sobrenome TEXT,
                email TEXT
            )
        ''')

        conexao.commit()
        conexao.close()

    def adicionar_cliente(self):
        tarefa = self.txt_nome.text()
        if tarefa:
            self.lst_cliente.addItem(tarefa)
            self.txt_nome.clear()

    def remover_cliente(self):
        item_select = self.lst_cliente.currentItem()
        if item_select:
            self.lst_cliente.takeItem(self.lst_cliente.row(item_select))

    def editar_cliente(self):
        if self.btn_editar.text() == 'Editar':
            if self.cliente_selecionado is not None:
                conexao = sqlite3.connect('cadastro_cliente.db')
                cursor = conexao.cursor()
                cursor.execute('SELECT nome, sobrenome, email FROM '
                               'clientes WHERE id = ?', self.cliente_selecionado['id'])
                cliente = cursor.fetchone()
                conexao.close()

                if cliente :
                    nome, sobrenome, email = cliente
                    self.txt_nome.setText(nome)
                    self.txt_sobrenome.setText(sobrenome)
                    self.txt_email.setText(email)
                    self.btn_editar.setText('Cancelar')
        else:
            self.txt_nome.clear()
            self.txt_sobrenome.clear()
            self.txt_email.clear()
            self.btn_editar.setText('Editar')

    def salvar_cliente(self):
        nome = self.txt_nome.text()
        sobrenome = self.txt_sobrenome.text()
        email = self.txt_email.text()

        if nome and sobrenome and email:
            conexao = sqlite3.connect('cadastro_cliente.db')
            cursor = conexao.cursor()

            if self.cliente_selecionado is None:
                cursor.execute('''
                            INSERT INTO clientes(nome, sobrenome, email)
                                VALUES (?, ?, ?)
                        ''', (nome, sobrenome, email))
            else:
                cursor.execute('''
                    UPDATE clientes
                    SET nome = ?, sobrenome = ?, email = ?
                    WHERE ID = ?
                ''', (nome, sobrenome, email, self.cliente_selecionado['id']))

            conexao.commit()
            conexao.close()

            # Limpar os campos
            self.txt_nome.clear()
            self.txt_sobrenome.clear()
            self.txt_email.clear()
            self.cliente_selecionado = None
            self.carregar_clientes()

        else:
            QMessageBox.warning(self, 'Aviso', 'Preencha todos os dados')


    def carregar_clientes(self):
        self.lst_cliente.clear()
        conexao = sqlite3.connect('cadastro_cliente.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome, sobrenome, email FROM clientes')
        cliente = cursor.fetchall()
        conexao.close()

        for cliente in cliente:
            id_cliente, nome, sobrenome, email = cliente
            self.lst_cliente.addItem(f'{id_cliente} | {nome} {sobrenome} | {email}')

    def selecionar_cliente(self, item):
        self.cliente_selecionado = {
            'id': item.text().split()[0],
            'nome': self.txt_nome.text(),
            'sobrenome': self.txt_sobrenome.text(),
            'email': self.txt_email.text()
        }



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CadastroCliente()
    window.show()
    sys.exit(app.exec())
