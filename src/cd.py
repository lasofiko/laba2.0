import os
from lg import lg
import shutil 
def cd_c(p):
    try:
        if p == '..':
            os.chdir('..')
        elif p == '~':
            os.chdir(os.path.expanduser('~'))
        else:
            os.chdir(p)
        print(f'Текущая папка: {os.getcwd()}')
        lg(f'cd {p}')
    except Exception as e:
        print(f'Ошибка: {e}')
        lg(f'cd {p}', False)