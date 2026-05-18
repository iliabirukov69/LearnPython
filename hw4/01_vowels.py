text = input("Введите текст: ")
vowels = "аеёиоуыэюя"
result = [char for char in text.lower() if char in vowels]
print("Список гласных букв:", result)
print("Длина списка:", len(result))
