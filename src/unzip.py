from lg import lg
import shutil
import os
import zipfile
def unzip_c(a):
    try:
        with zipfile.ZipFile(a, 'r') as zip_ref: 
            # открытие архива, 1- имя,
            #  2-режим (r-чтение), zip_ref - объект, через который происходит работа с содержимым, 
            #  with- автоматически закрывает архив после работы 
            zip_ref.extractall('.') # извлечение всех файлов
        lg(f"unzip {a}")
        print(f"Архив {a} распакован.")
    except Exception as e:
        lg(f"unzip {a}", str(e))
        print(f"Ошибка: {e}")

