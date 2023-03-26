from show_data import *
from find_data import *
from delete import *
from change import *


def menuHello():
    print("1.Добавить")
    print("2.Вывести всех")
    print("3.Поиск по фамилии")
    print("4.Изменения данных")
    print("5.Удаление данных")
    print("6.Выход")
    userInput = int(input())
    if userInput == 1:
        addData()
        return True
    if userInput == 2:
        printAll()
        return True
    if userInput == 3:
        find(input("Введите фамилию: "))
        return True
    if userInput == 4:
        old_name = (input ('Введите Фамилию, которую нужно заменить: '))
        new_name = (input ('Введите новую Фамилию: '))
        change (new_name,old_name)
        return True
    if userInput == 5:
        delete(input('Введите Фамилию или Имя, которые хотите удалить: '))
        return True
    if userInput == 6:
        return False


def addData():
    data = open('file.txt', 'a')
    print('\n'*100)
    first_name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    item = [first_name, second_name,  number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
    print('\n'*100)
