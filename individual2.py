a2a1 = int(input("Введите двузначное число a2a1: "))
b = int(input("Введите однозначное число b: "))

a2 = a2a1 // 10
a1 = a2a1 % 10
sum_ab = a2a1 + b
result_a2 = sum_ab // 10
result_a1 = sum_ab % 10

print(f"Цифры числа, равного сумме a2a1 и b: {result_a2}{result_a1}")
