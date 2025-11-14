from lg import lg
import shutil
import os

def rm_c(p):
    try:
        abs_path = os.path.abspath(p)
        if abs_path == '/' or abs_path == os.path.abspath('..'):
            print('Ошибка: Запрещено удалять корневой или родительский каталог')
            lg(f'rm {p}', False)
            return

        if os.path.isdir(p):
            otv = input(f"Удалить папку '{p}' и всё её внутри нее? (y/n): ")
            if otv.lower() == 'y':
                shutil.rmtree(p) # удаляем каталог, включая все подкаталоги и файлы.
                print(f"Папка '{p}' удалена")
                lg(f'rm {p}')
            else:
                print('Удаление отменено')
        else:
            os.remove(p)
            print(f"Файл '{p}' удален")
            lg(f'rm {p}')

    except FileNotFoundError:
        print(f"Ошибка: '{p}' не найден!")
        lg(f'rm {p}',False)

    except:
        print('Ошибка удаления!')
        lg(f'rm {p}',False)