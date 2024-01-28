from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

# Створюємо модель
model = LpProblem(name="optimal-product-schedule", sense=LpMaximize)

# Визначаємо змінні
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Додаємо функцію цілі (максимізація кількості вироблених продуктів)
model += lemonade + fruit_juice

# Додаємо обмеження
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")  # Обмеження води
model += (1 * lemonade <= 50, "Sugar_Constraint")  # Обмеження цукру
model += (1 * lemonade <= 30, "Lemon_Juice_Constraint")  # Обмеження лимонного соку
model += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")  # Обмеження фруктового пюре

# Розв'язуємо задачу
model.solve()

# Отримуємо та виводимо результати
lemonade_amount = lemonade.varValue
fruit_juice_amount = fruit_juice.varValue
status = LpStatus[model.status]

lemonade_amount, fruit_juice_amount, status
