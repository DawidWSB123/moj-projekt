tasks = []

def show_menu():
    print("\n--- TO DO APP ---")
    print("1. Dodaj zadanie")
    print("2. Pokaż zadania")
    print("3. Usuń zadanie")
    print("4. Wyjście")

def add_task():
    task = input("Wpisz nowe zadanie: ")
    tasks.append(task)
    print("Dodano zadanie.")

def show_tasks():
    if not tasks:
        print("Brak zadań.")
    else:
        print("Twoje zadania:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    show_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Usunięto zadanie: {removed}")
        else:
            print("Nieprawidłowy numer.")
    except ValueError:
        print("Wprowadź poprawny numer.")

def main():
    while True:
        show_menu()
        choice = input("Wybierz opcję: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Do widzenia!")
            break
        else:
            print("Nieznana opcja, spróbuj jeszcze raz.")

if __name__ == "__main__":
    main()
