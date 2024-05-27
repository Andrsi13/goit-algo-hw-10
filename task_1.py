import pulp


model = pulp.LpProblem("Максимізації виробництва", pulp.LpMaximize)  # Максимізація

# Змінні для кількості виробленого лимонаду та фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0)
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0)


# Обмеження ресурсів
water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40


# Додаємо цільову функцію: максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Загальна кількість напоїв"

# Додаємо обмеження на ресурси
model += 2 * lemonade + fruit_juice <= water, "Обмеження на воду"
model += lemonade <= sugar, "Обмеження на цукор"
model += lemonade <= lemon_juice, "Обмеження на лимонний сік"
model += 2 * fruit_juice <= fruit_puree, "Обмеження на фруктове пюре"

# Розв'язання моделі
model.solve()

# Виведення статусу рішення
print(f"Статус рішення: {pulp.LpStatus[model.status]}")

# Виведення значень змінних
for variable in model.variables():
    print(f"{variable.name} = {variable.varValue}")

# Вартість цільової функції
print(f"Загальна кількість вироблених напоїв = {pulp.value(model.objective)}")
