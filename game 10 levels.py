import random

class Level:
    def __init__(self, number):
        self.number = number
        self.resources = 0
        self.alive = True

    def receive(self, amount):
        if not self.alive:
            return 0
        self.resources += amount
        return self.resources

    def act(self):
        if not self.alive:
            print(f"Уровень {self.number} пропускаеш ход (мертв).")
            return 0

        print(f"\nУровень {self.number}")
        print(f"Текущие ресурсы: {self.resources}")
        print("что делать?")
        print("1. Забрать себе (все)")
        print("2. Поделиться (половину отдать дальше)")
        print("3. Передать всё дальше")

        while True:
            choice = input("Выбор (1-3): ")
            if choice in ['1', '2', '3']:
                break
            else:
                print("Пожалуйста, введите 1-3.")

        if choice == '1':
            action = "забрал  всё"
            sent = 0
        elif choice == '2':
            action = "поделился "
            sent = self.resources // 2
            self.resources -= sent
        else:
            action = "передалть дальше"
            sent = self.resources
            self.resources = 0

        loss = int(sent * 0.2)
        actual_sent = sent - loss

        print(f"{action}. Передано : {actual_sent} (потери: {loss})")
        return actual_sent

    def check_survival(self):
        if self.resources <= 0:
            self.alive = False
            print(f"Уровень {self.number} погиб.")
        else:
            print(f"Уровень {self.number} выжил (ресурсов: {self.resources})")
        return self.alive

class Game:
    def __init__(self, levels_count=10):
        self.levels = [Level(i + 1) for i in range(levels_count)]

    def start(self):
        current_resources = random.randint(100, 200)
        print(f"Начальные ресурсы: {current_resources}\n")

        round_number = 1
        while True:
            print(f"\nРаунд {round_number} ")
            current = current_resources
            current_resources = 0

            for level in self.levels:
                current = self.play_turn(level, current)
                level.check_survival()

            current_resources = current
            alive_levels = [l for l in self.levels if l.alive]
            all_alive = len(alive_levels) == len(self.levels)
            none_alive = len(alive_levels) == 0
            player_alive = self.levels[0].alive

           
            print("\n Статус :::")
            if player_alive:
                print("Ты жив.")
            else:
                print("Ты погиб.")

            if all_alive:
                print("Все живы.")
            elif none_alive:
                print("Все мертвы.")
            else:
                print("Некоторые погибли.")

            if none_alive or current_resources <= 0:
                print("\nИгра окончена.")
                break

            round_number += 1

        self.show_final_results()

    def play_turn(self, level, incoming):
        received = level.receive(incoming)
        return level.act()

    def show_final_results(self):
        print("\n Итоги :::")
        for level in self.levels:
            status = "в игре" if level.alive else "выбыл"
            print(f"Уровень {level.number}: {status}, остаток рес: {level.resources}")


game = Game()
game.start()
