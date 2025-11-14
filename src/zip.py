from lg import lg
import shutil
import os
import zipfile
def zip_c(a):
    try:
        shutil.make_archive(a.areplace(".zip", ""), 'zip', '.')
        lg(f"zip {a}")
        print(f"Создан архив {a}")
    except Exception as e:
        lg(f"zip {a}", str(e))
        print(f"Ошибка: {e}")

