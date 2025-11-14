from lg import lg
import shutil
import os

def cp_c(fr, t):
    try:
        if os.path.isdir(fr):
            shutil.copytree(fr, t)
        else:
            shutil.copy2(fr, t)
        print(f'Скопировано: {fr} → {t}')
        lg(f'cp {fr} {t}')

    except Exception as e:
        print(f'Error: {e}')
        lg(f'cp {fr} {t}', False)