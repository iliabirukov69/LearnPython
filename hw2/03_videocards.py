count = int(input("Количество видеокарт: "))
old_cards = []
for i in range(count):
    card = int(input(f"{i + 1} Видеокарта: "))
    old_cards.append(card)
print("\nСтарый список видеокарт:", old_cards)

max_card = max(old_cards)
new_cards = [card for card in old_cards if card != max_card]
print("Новый список видеокарт:", new_cards)
