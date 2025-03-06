import file_handler

def add_note(title, text):
    note = f"Название: {title}\nТекст: {text}"
    file_handler.append_note(note)
    print("Заметка добавлена!")

def show_notes():
    notes = file_handler.read_notes()
    if not notes or (len(notes) == 1 and notes[0].strip() == ""):
        print("Заметок пока нет.")
        return

    for note in notes:
        print(note)
        print("---")

def delete_note(title):
    notes = file_handler.read_notes()
    updated_notes = []
    found = False

    for note in notes:
        if note.startswith(f"Название: {title}\n"):
            found = True
            continue
        updated_notes.append(note)

    if found:
        file_handler.write_notes(updated_notes)
        print(f"Заметка '{title}' удалена.")
    else:
        print(f"Заметка '{title}' не найдена.")
