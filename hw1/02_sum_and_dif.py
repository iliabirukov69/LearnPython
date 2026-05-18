def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

number = int(input("Введите число: "))

sum_digits = sum_of_digits(number)
count = count_digits(number)
difference = sum_digits - count

print(f"Сумма чисел: {sum_digits}")
print(f"Количество цифр в числе: {count}")
print(f"Разность суммы и количества цифр: {difference}")
