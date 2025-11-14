from lg import lg
import shutil
import os
import tarfile
def tar_c(a):
    try:
        with tarfile.open(a, "w:gz") as tar:
            # 1- имя архива, 2- режим записи с gzip-сжатием
            tar.add('.', arcname=os.path.basename('.'))
            # добавляет в архив текущую директорию и все ее содержимопе 
            # arcname=os.path.basename('.') - задает имя корневой папки в архиве
        lg(f"tar {a}")
        print(f"Создан архив {a}")
    except Exception as e:
        lg(f"tar {a}", str(e))
        print(f"Ошибка: {e}")
