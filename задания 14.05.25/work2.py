from colorama import Fore, init
init(autoreset=True)

moods = {
    'радый': (Fore.YELLOW, '😊'),
    'грустный': (Fore.BLUE, '😔'),
    'плачеш': (Fore.CYAN, '😫'),
    'удивльон': (Fore.RED, '😲')
}

print("Привет! Как настроения?")

mood = input(" твоё настроения :(радый, грустный, плачеш, удивльон): ").lower().strip()


if mood in moods:
    color, emoji = moods[mood]
    print(color + f"настроетия {mood} {emoji}")
else:
    print(Fore.RED + "иди отсуда")
