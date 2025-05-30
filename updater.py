import requests, zipfile, os, sys, subprocess
from pathlib import Path

GITHUB_ZIP_URL = "https://github.com/TU_USUARIO/TU_REPO/releases/latest/download/hola_mundo.zip"
GITHUB_VERSION_URL = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/version.txt"

APP_DIR = Path(sys.argv[0]).parent
LOCAL_VERSION_PATH = APP_DIR / "version.txt"

def get_local_version():
    if not LOCAL_VERSION_PATH.exists():
        return "0.0.0"
    return LOCAL_VERSION_PATH.read_text().strip()

def get_remote_version():
    try:
        return requests.get(GITHUB_VERSION_URL, timeout=5).text.strip()
    except:
        return None

def check_for_update_and_run():
    local = get_local_version()
    remote = get_remote_version()
    if not remote:
        print("No se pudo comprobar la versión.")
        return

    if local != remote:
        print(f"Actualización disponible: {remote}")
        download_and_update()
    else:
        print("Todo actualizado.")

def download_and_update():
    zip_path = APP_DIR / "update.zip"
    with requests.get(GITHUB_ZIP_URL, stream=True) as r:
        with open(zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(APP_DIR)
    os.remove(zip_path)

    # Relanzar
    subprocess.Popen([sys.executable, os.path.basename(sys.argv[0])])
    sys.exit()

