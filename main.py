import os
import time

import requests
import shutil
from tqdm import tqdm
import zipfile


def unZipFile(fileName):
    with zipfile.ZipFile(fileName, 'r') as zip_ref:
        zip_ref.extractall("C:\\dev")


def getFile(url, fileName):
    response = requests.get(url, stream=True)

    total_size_in_bytes = int(response.headers.get('content-length', 0))

    progress_bar = tqdm(total=total_size_in_bytes, unit='B', unit_scale=True)

    if response.status_code == 200:
        with open(fileName, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                progress_bar.update(len(data))
                file.write(data)

        print(f"Archivo descargado exitosamente como {fileName}")
    else:
        print(f"No se pudo descargar el archivo. Código de estado: {response.status_code}")


def moveFile(fileName, goFolder):
    ruta_original = fileName
    ruta_destino = os.path.join(goFolder, fileName)

    shutil.move(ruta_original, ruta_destino)
    print(f"Archivo movido a {goFolder}")


urlFile = "https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.16.5-stable.zip"
nameFile = "flutterSdk.zip"
folder = "C:\\dev"

print("Descargando archivo...")
getFile(urlFile, nameFile)
time.sleep(2)
print("Moviendo " + nameFile + " a " + folder)
moveFile(nameFile, folder)
time.sleep(2)
print("Descomprimiendo " + nameFile)
unZipFile(os.path.join(folder, nameFile))
