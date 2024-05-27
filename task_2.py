import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()



#Розрахунок площі методом Монте-Карло

# Визначення розмірів прямокутника
x_max = b
y_max = f(b)

# Генерація випадкових точок
num_points = 15000
x_points = [random.uniform(a, x_max) for _ in range(num_points)]
y_points = [random.uniform(0, y_max) for _ in range(num_points)]

# Відбір точок, що знаходяться під кривою
inside_points = [(x, y) for x, y in zip(x_points, y_points) if y <= f(x)]

# Кількість усіх точок та точок під кривою
N = len(x_points)
M = len(inside_points)

# Площа прямокутника та площа під кривою, обчислена методом Монте-Карло
rectangle_area = (x_max - a) * y_max
area_under_curve = (M / N) * rectangle_area

# Виведення результатів
print(f"Кількість точок під кривою: {M}, загальна кількість точок: {N}")
print(f"Площа під кривою методом Монте-Карло: {area_under_curve}")

# Візуалізація
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, 400)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання точок
ax.scatter(x_points, y_points, color='blue', s=1, alpha=0.5)
ax.scatter(*zip(*inside_points), color='green', s=1, alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, y_max + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


#Перевірка првильності розрахунків за допопмогою функції quad

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)
