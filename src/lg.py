import os
from datetime import datetime
import shutil 
def lg(c, F=True):
    now = datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')

    if F:
        s = f'[{time}] {c}'
    else:
        s = f'[{time}] ОШИБКА: {c}'

    with open('shell.log', 'a', encoding='utf-8') as log:
        log.write(s + '\n')