import os
import shutil
import datetime
from ls import ls_c
from cd import cd_c
from cat import cat_c
from cp import cp_c
from rm import rm_c
from mv import mv_c

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
                    if len(s) > 1:
                        ls_c(' '.join(s[1:]))
                    else:
                        ls_c('.')
                case 'cd':
                    if len(s)>1:
                        p=s[1]
                        cd_c(p)
                    else:
                        print('Ошибка, укажите путь')
                case 'cat':
                    if len(s)>1:
                        p=s[1]
                        cat_c(p)
                    else:
                        print('Ошибка, укажите файл')
                case 'cp':
                     if len(s)>2:
                        cp_c(s[1],s[2])
                     else:
                         print('Oшибка, не указан источник и назначения')
                case 'rm':
                    if len(s)>1:
                        rm_c(s[1])
                    else:
                        print('Ошибка, не указано, что удалять')
                case 'mv':
                    if len(s)>2:
                        mv_c(s[1],s[2])
                    else:
                        print('Ошибка, не указан источник и назначения')
                case 'exit':
                    print('Пока')
                case _:
                    print(f'Неизвестная команда: {x}')

if __name__=='__main__':
    main()

