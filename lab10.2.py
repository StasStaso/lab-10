from datetime import date


class Memory:
    def __init__(self, producer, date, storage, price):
        self.producer = producer
        self.date = date
        self.storage = storage
        self.price = price

    def convert_to_gb(self):
        return self.storage / 1024

    def convert_to_kb(self):
        return self.storage * 1024

    def convert_to_byte(self):
        return self.storage * 1048576

    # 1 - bytes; 2-Kb; 3-Mb; 4-Gb
    def compare_storage(self, infosize, units):
        if units == 1:  # bytes
            if (self.convert_to_byte() - infosize) >= 0:
                return 'Так'
            return 'Ні'
        elif units == 2:  # Kb
            if (self.convert_to_kb() - infosize) >= 0:
                return 'Так'
            return 'Ні'
        elif units == 3:  # Mb
            if (self.storage - infosize) >= 0:
                return 'Так'
            return 'Ні'
        elif units == 4:  # Gb
            if(self.convert_to_gb() - infosize) >= 0:
                return 'Так'
            return 'Ні'

    def memory_age(self):
        diff = (date.today() - self.date).days
        return round((diff/365), 0)


mem = Memory('Kingston', date(2015, 7, 7), 8192, 1099)

print('Виберіть одиницю виміру: 1-bytes, 2-Kb, 3-Mb, 4-Gb')
units = int(input('Одиниця виміру: '))
size = int(input('Введіть обєм інформації: '))
if size > 0 and (units == 1 or units == 2 or units == 3 or units == 4):
    print('Чи поміститься обєм інформації: {0}'.format(mem.compare_storage(size, units)))
else:
    print('Спробуйте ще раз')

print('З дати виробництва пройшло {0} років'.format(mem.memory_age()))
print('Обєм - bytes: {0}, Kb: {1}, Mb: {2}, Gb: {3} '.format(mem.convert_to_byte(),
      mem.convert_to_kb(), mem.storage, mem.convert_to_gb()))



