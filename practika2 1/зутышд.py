import time
import os
from colorama import init, Fore, Style

# Инициализация colorama (важно для Windows)
init(autoreset=True)

# ASCII-арт члена
penis_art = [
    "    ()",
    "    ||",
    "    ||",
    "    ||",
    "   /||\\",
    "  / || \\",
    " /  ||  \\",
    "    ||",
    "    ||",
    "    /\\",
    "   /__\\",
    "  (____)"
]

# Цвета для фана
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def clear_screen():
    """Очищает экран в зависимости от ОС"""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_colored_penis():
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "ПРЕДУПРЕЖДЕНИЕ: Контент 18+!\n")

    # Постепенно печатаем каждую строку с цветами и задержкой
    for i, line in enumerate(penis_art):
        color = colors[i % len(colors)]
        print(color + line)
        time.sleep(0.3)

    # После завершения - ждём и добавляем забавное сообщение
    time.sleep(1)
    print(Fore.MAGENTA + Style.BRIGHT + "\nМогучий Python-член готов к бою!")

if __name__ == "__main__":
    draw_colored_penis()
