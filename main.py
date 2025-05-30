import sys
import subprocess
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from pathlib import Path

VERSION_LOCAL = Path(__file__).parent / "version.txt"
URL_VERSION = "https://raw.githubusercontent.com/larceing/hola_mundo_autoupdate/main/version.txt"

def get_local_version():
    return VERSION_LOCAL.read_text().strip() if VERSION_LOCAL.exists() else "0.0.0"

def get_remote_version():
    try:
        return requests.get(URL_VERSION, timeout=5).text.strip()
    except:
        return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo v" + get_local_version())
        self.setFixedSize(400, 200)

        label = QLabel("¡Hola Mundo!", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn = QPushButton("Buscar actualizaciones", self)
        btn.clicked.connect(self.buscar_actualizaciones)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def buscar_actualizaciones(self):
        local = get_local_version()
        remote = get_remote_version()
        if remote and remote != local:
            subprocess.Popen(["updater.exe"])
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
