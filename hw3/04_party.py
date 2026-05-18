guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")
    if action == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break
    elif action == "пришёл":
        name = input("Имя гостя: ")
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    elif action == "ушёл":
        name = input("Имя гостя: ")
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"Этого гостя нет на вечеринке.")
