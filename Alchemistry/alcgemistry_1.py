class AlchemyGame:
    def __init__(self):
        self.recipes = {
            ("вода", "земля"): "грязь",
            ("воздух", "огонь"): "молния",
            ("земля", "огонь"): "лава",
            ("вода", "огонь"): "пар"}
        self.inventory = ["вода", "земля", "воздух", "огонь"]

    def show_inventory(self):
        print("\nВаши элементы:")
        for item in self.inventory:
            print(f"- {item}")

    def mix_elements(self, elem1, elem2):
        if elem1 not in self.inventory or elem2 not in self.inventory:
            print("Ошибка: у вас нет одного из этих элементов!")
            return
        if elem1 > elem2:
            pair = (elem2, elem1)
        else:
            pair = (elem1, elem2)

        if pair in self.recipes:
            discovered = self.recipes[pair]
            if discovered not in self.inventory:
                self.inventory.append(discovered)
                print(f"Успех! Вы открыли новый элемент: {discovered}!")
            else:
                print(f"Вы получили {discovered}, но этот элемент у вас уже есть.")
        else:
            print("Ничего не произошло. Такие элементы не соединяются.")

    def run(self):
        print("Добро пожаловать в игру Алхимия!")
        while True:
            self.show_inventory()
            print("\nВведите два элемента для смешивания (или 'выход' для завершения):")
            
            first = input("Первый элемент: ").strip().lower()
            if first == "выход":
                break
                
            second = input("Второй элемент: ").strip().lower()
            if second == "выход":
                break

            self.mix_elements(first, second)
            input("\nНажмите Enter, чтобы продолжить...")

        print("\nСпасибо за игру! Итоговый список открытых элементов:")
        self.show_inventory()


if __name__ == "__main__":
    game = AlchemyGame()
    game.run()
