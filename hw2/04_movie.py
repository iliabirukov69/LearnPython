films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия",
    "Город грехов", "Мементо", "Отступники", "Деревня"]
count = int(input("Сколько фильмов хотите добавить? "))
user_favorites = []
for _ in range(count):
    film_name = input("Введите название фильма: ")
    if film_name in films:
        user_favorites.append(film_name)
    else:
        print(f"Ошибка: фильма {film_name} у нас нет :(")

print("Ваш список любимых фильмов:", ", ".join(user_favorites))
