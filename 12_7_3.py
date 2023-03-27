per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
list = list(per_cent.values())
a = list[0] * money
b = (list[1] * money)
c = (list[2] * money)
d = (list[3] * money)
deposit=[a,b,c,d]
max_deposit = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max_deposit)

