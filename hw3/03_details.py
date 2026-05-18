shop = [["каретка", 1200], ["шатун", 1000], ["седло", 300],
    ["педаль", 100], ["седло", 1500], ["рама", 12000],
    ["обод", 2000], ["шатун", 200], ["седло", 2700]]

search_item = input("Название детали: ")
count = 0
total_price = 0
for item, price in shop:
    if item == search_item:
        count += 1
        total_price += price

print("Кол-во деталей —", count)
print("Общая стоимость —", total_price)
