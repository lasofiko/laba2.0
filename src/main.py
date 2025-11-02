import os
import shutil
import datetime

def ls_c():
    allin=os.listdir()
    for i in allin:
        print(i)
def cd_c(p):
    try:
        os.chdir(p)
        print(f'  в папку {os.getcwd()}')
    except FileNotFoundError:
        print(f'папка не найдена')
    except PermissionError:
        print(f'нет доступа к папке')

def cat_c(p):
    try:
        # 1. Открыть файл для чтения
        with open(p, 'r', encoding='utf-8') as pt:
            # 2. Прочитать всё содержимое
            s = pt.read()
            # 3. Вывести на экран
            print(s)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{p}' не найден!")
    except:
        print(f"Ошибка: Не удалось прочитать файл '{p}'")

import shutil

def cp_c(fr, t):
    try:
        # Просто копируем файл
        shutil.copy2(fr, t)
        print(f"Скопировано: {fr} → {t}")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{fr}' не найден!")
    except:
        print("Ошибка копирования!")


def mv_c(fr, t):
    try:
        # Перемещаем файл
        shutil.move(fr, t)
        print(f"Перемещено: {fr} → {t}")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{fr}' не найден!")
    except:
        print("Ошибка перемещения!")


def rm_c(p):
    try:
        if os.path.isdir(p):
            # Если это папка - спрашиваем подтверждение
            ответ = input(f"Удалить папку '{p}' и всё её содержимое? (y/n): ")
            if ответ.lower() == 'y':
                shutil.rmtree(p)
                print(f"Папка '{p}' удалена")
            else:
                print("Удаление отменено")
        else:
            # Если это файл - просто удаляем
            os.remove(p)
            print(f"Файл '{p}' удален")
    except FileNotFoundError:
        print(f"Ошибка: '{p}' не найден!")
    except:
        print("Ошибка удаления!")




def lg_c(c, t=True):
    # Получаем текущее время
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Формируем запись
    if t:
        s = f"[{time}] {c}"
    else:
        s = f"[{time}] ОШИБКА: {c}"

    # Записываем в файл
    with open("shell.log", "a", encoding="utf-8") as lg:
        lg.write(s + "\n")




def main():
    while 1:
        a=input()
        s=a.split()

        if not s:
            continue
        if len(s):
            x=s[0].lower()
            match x:
                case 'ls':
                    ls_c()
                case 'cd':
                    p=s[3:]
                    cd_c(p)
                case 'cat':
                    p=s[4:]
                    cat_c(p)
                case 'cp':
                    p=s[5:]
                    cp_c(p)
                case 'rm':
                    p=s[6:]
                    rm_c(p)
                case 'mv':
                    p=s[7:]
                    mv_c(p)
                case 'exit':
                    print("By")
                case _:
                    raise NameError



if __name__== '__main__':
    main()



