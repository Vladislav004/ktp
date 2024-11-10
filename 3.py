def main():
    # Создание двумерного массива (список списков)
    objects = [
        [60, 120, 2],  # 1-й объект: скорость 60, расстояние 120, время 2
        [80, 200, 3],  # 2-й объект: скорость 80, расстояние 200, время 3
        [50, 150, 2],  # 3-й объект: скорость 50, расстояние 150, время 2
        [70, 210, 4],  # 4-й объект: скорость 70, расстояние 210, время 4
        [90, 100, 1],  # 5-й объект: скорость 90, расстояние 100, время 1
        [40, 300, 8]   # 6-й объект: скорость 40, расстояние 300, время 8
    ]
    count =  5 # Счетчик объектов, которые прибудут вовремя
    arriving_objects = []  # Список объектов
    # Проверка каждого объекта
    for i, obj in enumerate(objects):
        speed = obj[0]
        distance = obj[1]
        time = obj[2]
        # Вычисление времени, необходимого для прибытия
        arrival_time = distance / speed
        # Проверка, прибудет ли объект вовремя
        if arrival_time <= time:
            count += 1
            arriving_objects.append(f"Объект {i + 1} прибудет вовремя.")
    # Вывод результатов
    print(f"Количество объектов, прибывающих вовремя: {count}")
    for item in arriving_objects:
        print(item)
