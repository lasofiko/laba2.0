from lg import lg
import shutil
import os

def mv_c(fr, t):
    try:
        shutil.move(fr, t)
        print(f'Перемещено: {fr} → {t}')
        lg(f'mv {fr} {t}')

    except FileNotFoundError:
        print(f"Ошибка: Файл '{fr}' не найден!")
        lg(f'mv {fr} {t}', False)

    except:
        print('Ошибка перемещения!')
        lg(f'mv {fr} {t}', False)