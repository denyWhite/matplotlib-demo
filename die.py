from random import randint
import pygal

class Die():
    """Класс моделирующий игральный кубик"""
    def __init__(self, num_sides = 6):
        """
        Инициализация
        :param num_sides: Кол-во сторон, 6 по укмолчанию
        """
        self.num_sides = num_sides
    def roll(self):
        """
        Бросок кубика
        :return: Число
        """
        return randint(1, self.num_sides)


d = Die()
results = []
count = 1000000
for i in range(count):
    results.append(d.roll() + d.roll())
frequencies = []
for value in range(2, 2 * d.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
frequencies = list(map(lambda x: x / count , frequencies))
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000000 times."
hist.x_labels =  ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


