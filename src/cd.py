import os
from lg import lg
import shutil 
def cd_c(p):
    try:
        if p == '..':
            os.chdir('..') #переходит в родительскую папку
        elif p == '~':
            os.chdir(os.path.expanduser('~')) #преобразует ~ в полный путь к домашней папке
        else:
            os.chdir(p) #Переход в указанную директорию:
        print(f'Текущая папка: {os.getcwd()}')
        lg(f'cd {p}')
    except Exception as e:
        print(f'Ошибка: {e}')
        lg(f'cd {p}', False)
