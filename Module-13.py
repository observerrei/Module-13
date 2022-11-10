count_ticket = int(input("Введите количество билетов, которое Вы желаете приобрести: "))
age = []
sum_cost = 0
cost_baby = 0
cost_youth = 990
cost_old = 1390
for i in range(count_ticket):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        sum_cost += cost_baby
    elif 17 < age < 25:
        sum_cost += cost_youth
    else:
        sum_cost += cost_old
if count_ticket > 3:
    sum_cost = sum_cost - (sum_cost / 100 * 10)
print("Ваша сумма к оплате: ", sum_cost)
