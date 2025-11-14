import os
from lg import lg
import shutil
def cat_c(p):

    try:
        # проверка что путь ведет к файлу, а не к папке
        if os.path.isdir(p): #os.path.isdir(p) - проверяет, является ли путь директорией
            print(f"Ошибка: '{p}' является каталогом")
            lg(f'cat {p}', False)
            return
        with open(p, 'r', encoding='utf-8') as pt:
            s = pt.read()
            print(s)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{p}' не найден!")
        lg(f'cat {p}', False)
    except:
        print(f"Ошибка: Не удалось прочитать файл '{p}'")
        lg(f'cat {p}', False)

