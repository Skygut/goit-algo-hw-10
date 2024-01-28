from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

model = LpProblem(name="optimal-product-schedule", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice

model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")
model += (1 * lemonade <= 50, "Sugar_Constraint")
model += (1 * lemonade <= 30, "Lemon_Juice_Constraint")
model += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")
model.solve()

lemonade_amount = lemonade.varValue
fruit_juice_amount = fruit_juice.varValue
status = LpStatus[model.status]

print(f"Status: {status}")
print(f"Amount of Lemonade to produce: {lemonade_amount}")
print(f"Amount of Fruit Juice to produce: {fruit_juice_amount}")
