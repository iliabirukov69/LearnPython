count = int(input("Кол-во чисел: "))
numbers = []
for _ in range(count):
    numbers.append(int(input("Число: ")))
print("\nПоследовательность:", numbers)

start_index = 0
while start_index < len(numbers):
    sub_list = numbers[start_index:]
    if sub_list == sub_list[::-1]:
        break
    start_index += 1
to_add = numbers[:start_index][::-1]
print("Нужно приписать чисел:", len(to_add))
print("Сами числа:", to_add)
