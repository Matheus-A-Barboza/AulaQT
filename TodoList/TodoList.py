import sys

from PySide6.QtWidgets import QApplication, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QWidget


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

        self.btn_concluir = QPushButton('Concluir')
        self.btn_concluir.setStyleSheet("background-color: lightblue;"
                                        "border-radius: 5px;"
                                        "border: 2px solid blue;")

        self.btn_editar = QPushButton('Editar')
        self.btn_editar.setStyleSheet("background-color: #F1EB9C;"
                                        "border-radius: 5px;"
                                        "border: 2px solid yellow;")

        self.btn_remover = QPushButton('Remover')
        self.btn_remover.setStyleSheet("background-color: #FFA8A8;"
                                      "border-radius: 5px;"
                                      "border: 2px solid red;")

        self.lst_tarefa = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.txt_tarefa)
        layout.addWidget(self.btn_adicionar)
        layout.addWidget(self.btn_concluir)
        layout.addWidget(self.btn_editar)
        layout.addWidget(self.btn_remover)
        layout.addWidget(self.lst_tarefa)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication()
    app_lista_tarefas = AppListaTarefas()
    app_lista_tarefas.show()
    sys.exit(app.exec())