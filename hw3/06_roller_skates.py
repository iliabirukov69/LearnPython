skates_count = int(input("Кол-во коньков: "))
skates = []
for i in range(skates_count):
    skates.append(int(input(f"Размер {i + 1}-й пары: ")))
people_count = int(input("\nКол-во людей: "))
people = []
for i in range(people_count):
    people.append(int(input(f"Размер ноги {i + 1}-го человека: ")))

n = len(skates)
for i in range(n):
    for j in range(0, n - i - 1):
        if skates[j] > skates[j + 1]:
            skates[j], skates[j + 1] = skates[j + 1], skates[j]

m = len(people)
for i in range(m):
    for j in range(0, m - i - 1):
        if people[j] > people[j + 1]:
            people[j], people[j + 1] = people[j + 1], people[j]

skate_index = 0
person_index = 0
total_rented = 0
while skate_index < len(skates) and person_index < len(people):
    if skates[skate_index] == people[person_index]:
        total_rented += 1
        skate_index += 1
        person_index += 1
    elif skates[skate_index] < people[person_index]:
        skate_index += 1
    else:
        person_index += 1

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {total_rented}")
