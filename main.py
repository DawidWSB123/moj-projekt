tasks = []

def show_tasks():
    if not tasks:
        print("Brak zadań.")
    else:
        print("Twoje zadania:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Podaj nowe zadanie: ")
    tasks.append(task)
    print("Dodano zadanie.")

def remove_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Podaj numer zadania do usunięcia: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Usunięto zadanie: {removed}")
            else:
                print("Niepoprawny numer.")
        except ValueError:
            print("To nie jest numer.")

def main():
    while True:
        print("\nCo chcesz zrobić?")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Wyjdź")
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
