import os
from datetime import datetime
from lg import lg


def ls_c(p='.'):
    try:
        a = p.split()
        tp = '.'
        t = False

        for i in a:
            if i == '-l':
                t = True
            else:
                tp = i
        it = os.listdir(tp)
        # возвращает список файлов и папок в указанной директории

        if t:
            print(f'Содержимое {tp}:')
            for i in it:
                fp = os.path.join(tp, i)  # полный путь к файлу/папке
                st = os.stat(fp)  # получение метаданных
                sz = st.st_size  # размер в байтах
                dt = datetime.fromtimestamp(st.st_mtime)  # время изменения
                date_s = dt.strftime('%d.%m.%Y %H:%M')  # форматирование даты
                if os.path.isdir(fp):
                    print(f'папка   {sz:8} {date_s} {i}')
                else:
                    print(f'файл    {sz:8} {date_s} {i}')
        else:
            for i in it:
                fp = os.path.join(tp, i)
                if os.path.isdir(fp):
                    print(i + '/')
                else:
                    print(i)
        lg(f'ls {p}')

    except FileNotFoundError:
        print(f"Ошибка: Папка '{p}' не найдена")
        lg(f'ls {p}', False)
    except Exception as e:
        print(f'Ошибка: {e}')
        lg(f'ls {p}', False)           
