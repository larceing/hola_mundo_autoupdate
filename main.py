import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from updater import check_for_update_and_run

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo con Autoupdate")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()
        etiqueta = QLabel("¡Hola desde tu programa autoactualizable!")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_actualizar = QPushButton("Buscar actualizaciones")
        btn_actualizar.clicked.connect(check_for_update_and_run)

        layout.addWidget(etiqueta)
        layout.addWidget(btn_actualizar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

