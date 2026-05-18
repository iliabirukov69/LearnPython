import os

class Game:
    def __init__(self):
        self.player_count = 0
        self.names = []
        self.wins = []
        self.losses = []
        self.draws = []

    def setup(self):
        while True:
            num = input("Введите количество игроков (от 2 до 6): ")
            if num.isdigit() and 2 <= int(num) <= 6:
                self.player_count = int(num)
                break
            print("Пожалуйста, введите число от 2 до 6.")

        for i in range(1, self.player_count + 1):
            self.names.append(f"Игрок {i}")
            self.wins.append(0)
            self.losses.append(0)
            self.draws.append(0)

        os.system("cls" if os.name == "nt" else "clear")
        print("Игра начинается!")

    def get_move(self, name):
        while True:
            move = (
                input(f"{name}, ваш выбор (камень, ножницы, бумага): ")
                .strip()
                .lower()
            )
            if move in ["камень", "ножницы", "бумага"]:
                return move
            print("Неверный ввод. Попробуйте снова.")

    def resolve_round(self, choices):
        unique_moves = []
        for move in choices:
            if move not in unique_moves:
                unique_moves.append(move)

        if len(unique_moves) != 2:
            for i in range(self.player_count):
                self.draws[i] += 1
            return

        move1, move2 = unique_moves[0], unique_moves[1]
        winning_move = ""

        if (
            (move1 == "камень" and move2 == "ножницы")
            or (move1 == "ножницы" and move2 == "бумага")
            or (move1 == "бумага" and move2 == "камень")
        ):
            winning_move = move1
        else:
            winning_move = move2

        for i in range(self.player_count):
            if choices[i] == winning_move:
                self.wins[i] += 1
            else:
                self.losses[i] += 1

    def play_round(self):
        choices = []
        for i in range(self.player_count):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Ход: {self.names[i]}")
            move = self.get_move(self.names[i])
            choices.append(move)

            os.system("cls" if os.name == "nt" else "clear")
            print(
                f"{self.names[i]}, ваш ход принят. Передайте управление следующему игроку."
            )
            input("Нажмите Enter, чтобы продолжить...")

        os.system("cls" if os.name == "nt" else "clear")
        self.resolve_round(choices)

        print("=== Результаты раунда ===")
        for i in range(self.player_count):
            print(f"{self.names[i]} выбрал {choices[i]}")

        print("\n=== Текущая статистика ===")
        self.show_stats()
        print("========================")

    def show_stats(self):
        for i in range(self.player_count):
            print(f"{self.names[i]}: {self.wins[i]} побед, {self.losses[i]} поражений, {self.draws[i]} ничьих")
    def run(self):
        self.setup()
        while True:
            self.play_round()
            answer = input("Сыграть ещё раунд? (да/нет): ").strip().lower()
            if answer not in ["да", "yes", "д", "y"]:
                break
        print("\n=== ИТОГОВАЯ СТАТИСТИКА ===")
        self.show_stats()
        print("Спасибо за игру!")


if __name__ == "__main__":
    game = Game()
    game.run()
