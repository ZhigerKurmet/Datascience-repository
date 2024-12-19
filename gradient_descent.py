import numpy as np

# Функция потерь
def loss_function(x):
    return x**2 - 4*x + 6


# Производная функции потерь
def gradient(x):
    return 2*x - 4

# Градиентный спуск
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point
    trajectory = [x]  # Для сохранения пути оптимизации
    for _ in range(iterations):
        grad = gradient(x)  # Вычисляем градиент
        x = x - learning_rate * grad  # Обновляем параметр
        trajectory.append(x)
    return x, trajectory

# Начальные параметры
starting_point = 10  # Начальное значение x
learning_rate = 0.1  # Скорость обучения, "ADAM RMSPROP"
iterations = 3  # Количество итераций

# Выполняем градиентный спуск
optimal_x, trajectory = gradient_descent(starting_point, learning_rate, iterations)

# Печатаем результаты
print(f"Оптимальное значение x: {optimal_x}")
print(f"Значение функции потерь в оптимальной точке: {loss_function(optimal_x)}")

