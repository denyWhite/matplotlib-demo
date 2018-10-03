from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """Класс для генерирования случайных блужданий"""
    def __init__(self, num_points, step=5):
        """Инициализация"""
        self.num_points = num_points
        self.step = step
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        return choice([-1, 1]) * choice(range(self.step + 1))

    def fill_walk(self):
        """Заполняет все точки блуждания"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)


rw = RandomWalk(50000, 5)
rw.fill_walk()
plt.figure(figsize=(10, 6))
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolor='none', s=1)
plt.scatter(0, 0, c='red', edgecolors='none', s=2)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()


