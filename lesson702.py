#Домашнее задание по теме "Позиционирование в файле".
def custom_write(file_name, strings):
  strings_positions = {}
  with open(file_name, "w") as f:
    for i, string in enumerate(strings):
      current_position = f.tell()
      f.write(string + "\n")
      strings_positions[(i + 1, current_position + i)] = string
  return strings_positions

strings = [
  'Text for tell.',
  'Используйте кодировку utf-8.',
  'Because there are 2 languages!',
  'Спасибо!'
  ]
result = custom_write('test.txt', strings)
for elem in result.items():
  print(elem)
