initial_list = [1, 4, -3, 0, 10]
K = 3
print("Изначальный список:", initial_list)
N = len(initial_list)
K = K % N
shifted_list = initial_list[-K:] + initial_list[:-K]
print("Сдвинутый список:", shifted_list)
