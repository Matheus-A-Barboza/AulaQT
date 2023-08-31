import sys

from PySide6.QtWidgets import QApplication, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QWidget, QInputDialog
from PySide6.QtCore import Qt


class AppListaTarefas(QWidget):
    def __init__(self):
        super().__init__()

        self.tarefas = []

        self.setWindowTitle('To do List')
        self.setGeometry(100, 100, 400, 600)

        self.txt_tarefa = QLineEdit()

        self.btn_adicionar = QPushButton('Adicionar')
        self.btn_adicionar.setStyleSheet("background-color: lightgreen;"
                                         "border-radius: 5px;"
                                         "border: 2px solid green;")
        self.btn_adicionar.clicked.connect(self.adicionar_tarefas)

        self.btn_concluir = QPushButton('Concluir')
        self.btn_concluir.setStyleSheet("background-color: lightblue;"
                                        "border-radius: 5px;"
                                        "border: 2px solid blue;")
        self.btn_concluir.clicked.connect(self.concluir_tarefas)

        self.btn_editar = QPushButton('Editar')
        self.btn_editar.setStyleSheet("background-color: #F1EB9C;"
                                        "border-radius: 5px;"
                                        "border: 2px solid yellow;")
        self.btn_editar.clicked.connect(self.editar_tarefas)

        self.btn_remover = QPushButton('Remover')
        self.btn_remover.setStyleSheet("background-color: #FFA8A8;"
                                      "border-radius: 5px;"
                                      "border: 2px solid red;")
        self.btn_remover.clicked.connect(self.remover_tarefas)

        self.lst_tarefa = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.txt_tarefa)
        layout.addWidget(self.btn_adicionar)
        layout.addWidget(self.btn_concluir)
        layout.addWidget(self.btn_editar)
        layout.addWidget(self.btn_remover)
        layout.addWidget(self.lst_tarefa)

        self.setLayout(layout)

    def adicionar_tarefas(self):
        tarefa = self.txt_tarefa.text()
        if tarefa:
            self.lst_tarefa.addItem(tarefa)
            self.txt_tarefa.clear()

    def concluir_tarefas(self):
        item_select = self.lst_tarefa.currentItem()
        if item_select:
            item_select.setFlags(item_select.flags() | Qt.ItemIsUserCheckable)
            item_select.setCheckState(Qt.Checked)
            item_select.setFlags(~ Qt.ItemIsSelectable)
            item_select.setFlags(~ Qt.ItemIsEnabled)

    def remover_tarefas(self):
        item_select = self.lst_tarefa.currentItem()
        if item_select:
            self.lst_tarefa.takeItem(self.lst_tarefa.row(item_select))


    def editar_tarefas(self):
        item_select = self.lst_tarefa.currentItem()
        if item_select:
            novo_texto, ok = QInputDialog.getText(self, 'Editar tarefa','Editar a tarefa', text=item_select.text())
            if ok and novo_texto:
                item_select.setText(novo_texto)

if __name__ == '__main__':
    app = QApplication()
    app_lista_tarefas = AppListaTarefas()
    app_lista_tarefas.show()
    sys.exit(app.exec())