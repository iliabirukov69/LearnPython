import math

def find_min_divisor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n
  
number = int(input("Введите число: "))

if number > 1:
    min_divisor = find_min_divisor(number)
    print(f"Наименьший делитель, отличный от единицы: {min_divisor}")
else:
    print("Число должно быть больше 1")
