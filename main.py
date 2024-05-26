import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other, target):
        if other.defend() != target:
            other.health -= self.attack_power
            print(f"{self.name} атакует {other.name} в {target} и наносит {self.attack_power} урона.")
        else:
            print(f"{other.name} защитился от атаки в {target}!")

        if other.health < 0:
            other.health = 0
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def defend(self):
        return random.choice(["голова", "туловище", "конечности"])

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Дракон"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def get_target(self):
        target_options = {
            "1": "голова",
            "2": "туловище",
            "3": "конечности"
        }
        while True:
            choice = input("Выберите цель для атаки (1-голова, 2-туловище, 3-конечности): ")
            if choice in target_options:
                return target_options[choice]
            else:
                print("Неправильный выбор. Пожалуйста, выберите 1, 2 или 3.")

    def get_defense(self):
        defense_options = {
            "1": "голова",
            "2": "туловище",
            "3": "конечности"
        }
        while True:
            choice = input("Выберите зону защиты (1-голова, 2-туловище, 3-конечности): ")
            if choice in defense_options:
                return defense_options[choice]
            else:
                print("Неправильный выбор. Пожалуйста, выберите 1, 2 или 3.")

    def start(self):
        print("Начало игры!")
        turn = random.choice(["player", "computer"])

        while self.player.is_alive() and self.computer.is_alive():
            if turn == "player":
                target = self.get_target()
                self.player.attack(self.computer, target)
                turn = "computer"
            else:
                print("Дракон атакует!")
                defense = self.get_defense()
                computer_target = random.choice(["голова", "туловище", "конечности"])
                if computer_target != defense:
                    self.player.health -= self.computer.attack_power
                    print(f"Дракон атакует в {computer_target} и наносит {self.computer.attack_power} урона.")
                else:
                    print(f"Вы защитились от атаки в {computer_target}!")

                if self.player.health < 0:
                    self.player.health = 0
                print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")
                turn = "player"

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
