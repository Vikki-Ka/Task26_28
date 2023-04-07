from data_create import *


def input_data():
    lastname = last_name()
    firstname = first_name()
    phonenum = phone()

    with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "a", encoding="utf-32") as file:

        file.write(f"\n{lastname}\t{firstname}\t{phonenum}")


def print_data():
    with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "r", encoding="utf-8") as data:
        data_new = data.read()
        print(data_new)


def search():
    lookfor = input("кого ищем? ")
    bool_1 = False
    with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
                bool_1 = True
        if bool_1 == False:
            print(" такой записи нет ")


def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "a+", encoding="utf-8") as data_1:
            data_1.write("\n")
            for line in data:
                if line not in data_1:
                    data_1.write(line)


def delete_line():
    line_str = input("Введите запись, которую нужно удалить: ")
    with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "w", encoding="utf-8") as data1:
            for line in lines:
                if line_str not in line:
                    data1.write(line)
                else:
                    print(line)
                    ask = input("Желаете удалить эту строку (y,n) : ")
                    while ask not in ("y", "n"):
                        print("ввод некорректный")
                        ask = input("Желаете удалить эту строку (y,n) : ")
                    if ask == "n":
                        data1.write(line)


def change_line():
    line_str = input("Введите запись, которую нужно изменить: ")
    with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open('C:\Users\user\Documents\My\GeekBrains\Программирование\Python\HW-5\Task38\phonebook.txt', "w", encoding="utf-8") as data1:
            for line in lines:
                if line_str not in line:
                    data1.write(line)
                else:
                    ask = input("Что хотите поменять (1,2,3) : ")
                    while ask not in ("1", "2", "3"):
                        print("ввод некорректный")
                        ask = input("Что хотите поменять (1,2,3) : ")
                    new_data = input("Введите новые данные : ")
                    line_list = line.split()
                    line_list[int(ask)-1] = new_data
                    data1.write("\t".join(line_list)+"\n")


print_data()
