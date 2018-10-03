"""Построение простых графиков"""
import matplotlib.pyplot as plt

# Построение графика
squares = [i * i for i in range(1, 10)]
plt.plot(range(1, 10), squares, linewidth = 5)

plt.title("Square numbers", fontsize=24)
plt.xlabel("Values", fontsize=24)
plt.ylabel("Squares", fontsize=20)
plt.tick_params(axis="both", which="major", labelsize=14)
#plt.axes([1,10,1,100])

# Нанесение отдельных точки
plt.scatter(2, 4, s=200)

# Нанесение серии точек
values = range(1,5)
cubes = [i ** 3 for i in values]
plt.scatter(values, cubes, c='red', edgecolor='none', s=40)

plt.show()
