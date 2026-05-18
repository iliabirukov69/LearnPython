n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))

people = list(range(1, n + 1))
index = 0
while len(people) > 1:
    index = (index + k - 1) % len(people)
    people.pop(index)

print("\nОстался человек под номером", people[0])
