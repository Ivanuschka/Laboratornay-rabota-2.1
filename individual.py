import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

mod_a = abs(a)
mod_b = abs(b)

average_arithmetic = (mod_a + mod_b) / 2

average_geometric = math.sqrt(mod_a * mod_b)

# Вывод результатов
print(f"Среднее арифметическое модулей: {average_arithmetic}")
print(f"Среднее геометрическое модулей: {average_geometric}")
