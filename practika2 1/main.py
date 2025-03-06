import notes_manager

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Просмотреть все заметки")
        print("3. Удалить заметку")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название заметки: ")
            text = input("Введите текст заметки: ")
            notes_manager.add_note(title, text)
        elif choice == '2':
            notes_manager.show_notes()
        elif choice == '3':
            title = input("Введите название заметки для удаления: ")
            notes_manager.delete_note(title)
        elif choice == '4':
            print("Выход...")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

print("Запуск программы  тупой ты еблан  'Заметки'")
main()
