import math

def calculate_series_sum(x, eps):
    sum_series = 0.0
    term = x  # Начальный элемент ряда
    i = 1

    while abs(term) > eps:
        sum_series += term
        # Рекуррентное соотношение для следующего элемента ряда
        term *= -x * (1.0 + 1.0 / i) / (i + 1)
        i += 1

    return sum_series

# Основная программа
x = 0.5  # Значение x, для которого вычисляем сумму ряда
eps = 1e-6  # Заданная точность eps

series_sum = calculate_series_sum(x, eps)
control_sum = math.log(1 + x) - math.exp(-x) + 1

print("Сумма ряда с заданной точностью:", series_sum)
print("Контрольная сумма:", control_sum)
print("Разница:", abs(series_sum - control_sum))
