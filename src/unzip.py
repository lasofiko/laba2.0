from lg import lg
import shutil
import os
import zipfile
def unzip_c(a):
    try:
        with zipfile.ZipFile(a, 'r') as zip_ref: 
            # zip_ref - объект, через который происходит работа с содержимым, 
            zip_ref.extractall('.') # извлечение всех файлов
        lg(f"unzip {a}")
        print(f"Архив {a} распакован.")
    except Exception as e:
        lg(f"unzip {a}", str(e))
        print(f"Ошибка: {e}")

