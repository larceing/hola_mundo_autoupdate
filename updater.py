import os, sys, time, zipfile, requests, subprocess
from pathlib import Path

GITHUB_ZIP_URL = "https://github.com/larceing/hola_mundo_autoupdate/releases/latest/download/hola_mundo.zip"
APP_DIR = Path(os.getenv("PROGRAMFILES")) / "HolaMundo"
ZIP_PATH = APP_DIR / "update.zip"
LOG_PATH = APP_DIR / "update.log"

def log(msg):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def descargar_zip():
    try:
        with requests.get(GITHUB_ZIP_URL, stream=True) as r:
            with open(ZIP_PATH, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        log("Descarga completada.")
    except Exception as e:
        log(f"ERROR durante descarga: {e}")

def reemplazar_archivos():
    time.sleep(2)  # da tiempo a que se cierre main.exe
    try:
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(APP_DIR)
        os.remove(ZIP_PATH)
        log("Archivos reemplazados correctamente.")
    except Exception as e:
        log(f"ERROR al descomprimir: {e}")

def relanzar():
    try:
        subprocess.Popen([str(APP_DIR / "main.exe")])
        log("main.exe relanzado.")
    except Exception as e:
        log(f"ERROR al relanzar: {e}")
    sys.exit()

if __name__ == "__main__":
    descargar_zip()
    reemplazar_archivos()
    relanzar()
