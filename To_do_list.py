
import os
FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return[]
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print ("Список задач пуст")
    for index, task in enumerate(tasks, start=1):
        print (f"{index}. {task}")

def display_tasks(tasks):
    show_tasks(tasks)
    input ("\nНажмите Enter, чтобы вернуться в меню...\n")

def add_task(tasks):
    task = input("\nВведите новую задачу: ")
    tasks.append(task)
    print ("Задача добавлена\n")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nВведите номер задачи для удаления: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index-1)
            print (f"{removed} задача удалена\n")
        else:
            print ("Неверный номер\n")
    except ValueError:
        print ("Введите корректное число\n")

def main():
    tasks = load_tasks()
    while True:
        print ("===== Меню =====")
        print ("1. Показать задачи")
        print ("2. Добавить задачу")
        print ("3. Удалить задачу")
        print ("4. Выход")
        choice = input ("\nДействие номер: ")
        if choice =="1":
            print ()
            display_tasks(tasks)
        elif choice =="2":
            add_task(tasks)
        elif choice =="3":
            print ()
            remove_task(tasks)
        elif choice =="4":
            save_tasks(tasks)
            print ("Сохранено. Выход")
            break
        else:
            print ("Неверный выбор\n")

if __name__ == "__main__":
    main()