count = int(input("Количество контейнеров: "))
containers = []
for i in range(count):
    while True:
        weight = int(input("Введите вес контейнера: "))
        if weight <= 200:
            containers.append(weight)
            break
        print("Ошибка: вес не должен превышать 200. Попробуйте снова.")
while True:
    new_container = int(input("\nВведите вес нового контейнера: "))
    if new_container <= 200:
        break
    print("Ошибка: вес не должен превышать 200. Попробуйте снова.")

position = 1
for weight in containers:
    if weight >= new_container:
        position += 1
    else:
        break
print("\nНомер, который получит новый контейнер:", position)
