tasks = []

def show_tasks():
    if not tasks:
        print("Brak zadań.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Dodaj zadanie: ")
    tasks.append(task)
    print("Dodano zadanie.")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Usunięto zadanie: {removed}")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Wpisz poprawny numer.")

def main():
    while True:
        print("\n1. Pokaż zadania\n2. Dodaj zadanie\n3. Usuń zadanie\n4. Wyjście")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Do widzenia!")
            break
        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()
