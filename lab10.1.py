class GeometricProgression:
    def __init__(self, b1, q):
        self.b1 = b1  # перший елемент
        self.q = q  # знаменник

    def print_first_element(self):
        print('Перший елемент = {0}'.format(self.b1))

    def print_ratio(self):
        print('Знаменник = {0}'.format(self.q))

    def get_n_element(self, n):
        bn = self.b1 * self.q ** (n-1)
        return bn

    def get_sum(self, n):
        if self.q > 1:
            sn = (self.b1 * (self.q**n - 1)) / (self.q - 1)
        else:  # якщо геом. прогресія є нескінченно спадною
            sn = self.b1 / (1 - self.q)
        return sn


b1 = float(input('Введіть перший елемент: '))
q = float(input('Введіть знаменник геом. прогр.: '))
gp = GeometricProgression(b1, q)
gp.print_first_element()  # вивід першого елемента
gp.print_ratio()  # вивід знаменника

n = int(input('Введіть n: '))
print('b({0}) = {1}'.format(n, gp.get_n_element(n)))  # обчислення n-го елемента
print('Сума перших {0} членів геом. прогр. = {1}'.format(n, gp.get_sum(3)))  # сума перших n елементів


