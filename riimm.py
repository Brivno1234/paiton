from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    @abstractmethod
    def vois(self):
        pass


class Hrest(Person):
    def __init__(self, name, strength, hrest_add):
        super().__init__(name, strength)
        self.hrest_add = hrest_add

    def vois(self):
        return f"\nхрестианин: {self.name} сила: {self.strength}"


class Gladiator(Person):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.legion = []

    def vois(self):
        return f"{self.name}: генерал и гладиатор ,сила: {self.strength}"

    def verbovat(self, hrest):
        print(hrest.vois())
        if hrest.hrest_add and len(hrest.name) > 2:
            if len(self.legion) < 10:
                self.legion.append(hrest)
                print(f"{hrest.name} вступил в легион.")
            else:
                print("Легион полон.")
        else:
            print(f"{hrest.name} отказался.")

    def legionInfo(self):
        if not self.legion:
            print("Легион пуст.")
        for bojec in self.legion:
            print(f"- {bojec.name}, сила {bojec.strength}")

    def level_legion(self):
        print("\nТренировка легиона...")
        for bojec in self.legion:
            bojec.strength += 2
        print("Легион стал сильнее.")


vileg = [
    {
        "vileg_name": "vileg1",
        "atack": False,
        "Hrest": [
            Hrest("mer", 6, True),
            Hrest("kat", 4, True),
            Hrest("dod", 7, True)
        ]
    },
    {
        "vileg_name": "vileg2",
        "atack": True,
        "Hrest": [
            Hrest("Mert", 8, True),
            Hrest("kuala", 5, False)
        ]
    },
    {
        "vileg_name": "vileg3",
        "atack": False,
        "Hrest": [
            Hrest("farm", 9, True),
            Hrest("kjfkf", 3, True)
        ]
    }
]

gladiator = Gladiator("lubimcev",11)

for vilegs in vileg:
    print(f"\n--- {vilegs['vileg_name']} ---")
    if vilegs["atack"]:
        print(f"Деревня враждебна. {gladiator.name} идёт дальше.")
        continue
    for krest in vilegs["Hrest"]:
        gladiator.verbovat(krest)

print(gladiator.vois())
gladiator.legionInfo()
gladiator.level_legion()
gladiator.legionInfo()
