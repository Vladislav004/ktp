import numpy as np


def process_arrays(X, Y):
    count = 0
    for i in range(len(X)):
        if X[i] >= Y[i]:
            Y[i] = X[i] - Y[i]
        else:
            Y[i] = Y[i] - X[i]

        if X[i] == Y[i]:
            count += 1

    return Y, count


# Пример массивов
X = np.array([1, 5, 3, 7, 2])
Y = np.array([4, 3, 5, 2, 8])

# Обработка массива Y на основе условия
Y_processed, equality_count = process_arrays(X, Y)

# Вывод результатов
print("Обработанный массив Y:", Y_processed)
print("Количество случаев равенства Xi и Yi:", equality_count)
