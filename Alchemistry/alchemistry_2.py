import tkinter as tk
from tkinter import messagebox

class AlchemyGame:
    def __init__(self):
        self.recipes = {
            ("вода", "земля"): "грязь",
            ("воздух", "огонь"): "молния",
            ("земля", "огонь"): "лава",
            ("вода", "огонь"): "пар",
        }
        self.inventory = ["вода", "земля", "воздух", "огонь"]
      
        self.window = tk.Tk()
        self.window.title("Игра Алхимия")
        self.window.geometry("400x450")

        self.label_inv = tk.Label(
            self.window, text="Ваш инвентарь:", font=("Arial", 12, "bold")
        )
        self.label_inv.pack(pady=5)

        self.listbox = tk.Listbox(self.window, font=("Arial", 11), height=8)
        self.listbox.pack(fill=tk.BOTH, padx=20, pady=5)

        self.label_select = tk.Label(
            self.window,
            text="Выберите два элемента из списка выше:",
            font=("Arial", 10),
        )
        self.label_select.pack(pady=5)

        self.label_elem1 = tk.Label(
            self.window, text="Элемент 1: [не выбран]", font=("Arial", 10)
        )
        self.label_elem1.pack()
        self.selected_elem1 = ""

        self.label_elem2 = tk.Label(
            self.window, text="Элемент 2: [не выбран]", font=("Arial", 10)
        )
        self.label_elem2.pack()
        self.selected_elem2 = ""

        self.btn_select = tk.Button(
            self.window, text="Выбрать элемент", command=self.select_element
        )
        self.btn_select.pack(pady=5)

        self.btn_mix = tk.Button(
            self.window,
            text="Смешать элементы",
            command=self.mix_elements,
            bg="lightgreen",
        )
        self.btn_mix.pack(pady=5)

        self.btn_clear = tk.Button(
            self.window, text="Сбросить выбор", command=self.clear_selection
        )
        self.btn_clear.pack(pady=5)

        self.update_inventory_display()

    def update_inventory_display(self):
        self.listbox.delete(0, tk.END)
        for item in self.inventory:
            self.listbox.insert(tk.END, item)

    def select_element(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Внимание", "Сначала выберите элемент в списке!")
            return

        chosen = self.listbox.get(selection[0])

        if not self.selected_elem1:
            self.selected_elem1 = chosen
            self.label_elem1.config(text=f"Элемент 1: {chosen}")
        elif not self.selected_elem2:
            self.selected_elem2 = chosen
            self.label_elem2.config(text=f"Элемент 2: {chosen}")
        else:
            messagebox.showinfo(
                "Информация", "Оба элемента уже выбраны. Сбросьте выбор или смешайте."
            )

    def clear_selection(self):
        self.selected_elem1 = ""
        self.selected_elem2 = ""
        self.label_elem1.config(text="Элемент 1: [не выбран]")
        self.label_elem2.config(text="Элемент 2: [не выбран]")

    def mix_elements(self):
        if not self.selected_elem1 or not self.selected_elem2:
            messagebox.showwarning("Ошибка", "Необходимо выбрать два элемента!")
            return

        elem1 = self.selected_elem1
        elem2 = self.selected_elem2

        if elem1 > elem2:
            pair = (elem2, elem1)
        else:
            pair = (elem1, elem2)

        if pair in self.recipes:
            discovered = self.recipes[pair]
            if discovered not in self.inventory:
                self.inventory.append(discovered)
                self.update_inventory_display()
                messagebox.showinfo(
                    "Успех!", f"Вы открыли новый элемент: {discovered}!"
                )
            else:
                messagebox.showinfo(
                    "Результат",
                    f"Вы получили {discovered}, но этот элемент у вас уже есть.",
                )
        else:
            messagebox.showerror(
                "Неудача", "Ничего не произошло. Такие элементы не соединяются."
            )

        self.clear_selection()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = AlchemyGame()
    game.run()
