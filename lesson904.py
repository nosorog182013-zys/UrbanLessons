from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda a, b: a == b, first, second)))

def get_advanced_writer(file_name):
  def write_everything(*data_set):
    return file_name.write('\n'.join(map(str, data_set)))
  return write_everything

with open('example.txt', 'w') as file:
  write = get_advanced_writer(file)
  write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('ваш', 'код', 'полноценно', 'демонстрировал', 'логику', 'написанного')
print(first_ball())
print(first_ball())
print(first_ball())

