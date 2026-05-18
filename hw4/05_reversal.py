text = input("Введите строку: ")
first_h = text.find("h")
last_h = text.rfind("h")
between_reversed = text[first_h + 1 : last_h][::-1]
print( "Развёрнутая последовательность между первым и последним h:", between_reversed )
