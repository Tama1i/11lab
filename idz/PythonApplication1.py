
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def add(pep):
     # Запросить данные о работнике.
    name = input("name faname? ")
    num = int(input("number? "))
    br = int(input("burftday? "))

        # Создать словарь.
    chel = {
            'name': name,
            'num': num,
            'br': br,
            }

            # Добавить словарь в список.
    pep.append(chel)
            # Отсортировать список в случае необходимости.
    if len(pep) > 1:
        pep.sort(key=lambda item: item.get('br',''))
    return pep

def li(pep):
     line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
     print(line)
     print(
          '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
          "№",
          "F.I.O.",
          "NUMBER",
          "BRDAY"
          )
     )
     print(line)
     for idx, chel in enumerate(pep, 1):
        print(
             '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
             idx,
             chel.get('name', ''),
             chel.get('num', ''),
             chel.get('br', 0)
             )
        )
        print(line)


def sel(pep,zapros):
            # Инициализировать счетчик.
     count = 0
            # Проверить сведения работников из списка.
     for chel in pep:
        if chel.get('num') == zapros:
            count += 1
            return chel.get, count
            #print(
            #     '{:>4}: {}'.format(count, chel.get('name', ''))
            #)

            # Если счетчик равен 0, то работники не найдены.
     if count == 0:
        return "cheela s takim nomerom net", count

from datetime import date
if __name__ == '__main__':
    # Список работников.
    pep = []
    s = ""
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            pep = add(pep)

        elif command == 'list':
            li(pep)
        elif command == 'select':
            zapros = int(input("zapros po numeru  "))
            s, count = sel(pep,zapros)
            print(
                 '{:>4}: {}'.format(count, s('name', ''))
            )
            
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - add chel;")
            print("list - show list of pep;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


