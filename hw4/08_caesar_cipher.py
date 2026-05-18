text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper = alphabet.upper()
encrypted_text = []
for char in text:
    if char in alphabet:
        index = (alphabet.index(char) + shift) % len(alphabet)
        encrypted_text.append(alphabet[index])
    elif char in alphabet_upper:
        index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
        encrypted_text.append(alphabet_upper[index])
    else:
        encrypted_text.append(char)
print("Зашифрованное сообщение:", "".join(encrypted_text))
