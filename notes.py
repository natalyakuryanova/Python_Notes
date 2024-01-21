from datetime import datetime
import os

file_name = "notes"
file_ext = "csv"
filename = f'{file_name}.{file_ext}'

def get_id():
    notes = file_read().rstrip().split("\n")
    note = notes[-1]
    
    id = 0
    if note:
        info = note.replace("\n", " ").split(";")
        id = int(info[0])

    id += 1
    return id
    

def file_read():
    global file
    with open(filename, "r", encoding="UTF-8") as file:
        return file.read()


def file_append(text=""):
    global file
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)


#################################################
############## INPUT ############################
#################################################
def input_note():
    title = input("Введите Название: ")
    desc = input("Введите Заметку: ")
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    id = get_id()

    note_str = f"{id};{title};{desc};{date}\n" 
    file_append(note_str)

    print()


#################################################
############## PRINT ############################
#################################################
def print_notes():
    print(file_read())


#################################################
############## SEARCH ###########################
#################################################
def search_note():
    print("Возможные варианты поиска:\n"
          "1. По id\n"
          "2. По названии\n"
          "3. По описанию\n"
          "4. По дате\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2", "3", "4"):
        print("Некорректный ввод, повторите попытку")
        command = input("Выберите вариант поиска: ")

    i = int(command) - 1

    search = input("Введите данные для поиска: ")
    print()
    notes = file_read().rstrip().split("\n")

    for note in notes:
        info = note.replace("\n", " ").split(";")
        if search in info[i]:
            print(note)
            print()

#################################################
############## DELETE ###########################
#################################################
def delete_note():
    id = input("Введите ID удаляемой заметки: ")
    notes_str = file_read()
    notes = notes_str.rstrip().split("\n")

    note_to_delete = ""
    for note in notes:
        info = note.replace("\n", " ").split(";")
        if id == info[0]:
            print("DELETING: "+note)
            note_to_delete = note
            break

    if note_to_delete:
        new_data = notes_str.replace(note_to_delete+"\n", "")
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(new_data)
        print("Данные успешно удалены")
        print()

#################################################
############## EDIT #############################
#################################################
def edit_note():
    i_var = 0

    id = input("Введите ID удаляемой заметки: ")
    notes_str = file_read()
    notes = notes_str.rstrip().split("\n")
    
    for note in notes:
        info = note.replace("\n", " ").split(";")
        if id == info[0]:
            print("EDITING: "+note)
            break

    print("Выберите пункт, который необходимо отредактировать\n"
          "1. Название\n"
          "2. Описание\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2"):
        print("Некорректный ввод, повторите попытку")
        command = input("Выберите вариант поиска: ")

    edit_name = input("Введите данные для редактирования: ")
    info[int(command)] = edit_name
    note_new =";".join(info)
    
    new_data = notes_str.replace(note, note_new)

    with open(filename, "w", encoding="UTF-8") as file:
        file.write(new_data)
    print("Данные успешно изменены")
    print()


#################################################
############## START ############################
#################################################
def start():
    file_append()  
    command = ""
    while command != "6":
        print("Меню:\n"
              "1. Добавить заметку\n"
              "2. Найти заметку\n"
              "3. Вывести все заметки\n"
              "4. Редактировать заметку\n"
              "5. Удалить заметку\n"
              "6. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод, повторите попытку")
            command = input("Выберите пункт меню: ")

        print()
        match command:
            case "1":
                input_note()
            case "2":
                search_note()
            case "3":
                print_notes()
            case "4":
                edit_note()
            case "5":
                delete_note()
            case "6":
                print("Всего хорошего!")

start()