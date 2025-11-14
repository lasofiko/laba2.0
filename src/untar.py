from lg import lg
import shutil
import os
import tarfile

def untar_c(a):
    try:
        with tarfile.open(a, "r:gz") as tar:
            # gzip-сжатый tar-архива
            tar.extractall('.')
            # извлекает все файлы из архива в текущую директорию 
        lg(f"untar {a}")
        print(f"Архив {a} распакован.")
    except Exception as e:
        lg(f"untar {a}", str(e))
        print(f"Ошибка: {e}")
