#Домашнее задание по теме "Позиционирование в файле".
def custom_write(file_name, strings):
  strings_positions = {}
  with open(file_name, "w") as f:
    for i, string in enumerate(strings):
      f.write(string + "\n")
      current_position = f.tell()
      start_position = current_position - len(string) - 1
      strings_positions[(i + 1, start_position)] = string
  return strings_positions

strings = [
  'Text for tell.',
  'Используйте кодировку utf-8.',
  'Because there are 2 languages!',
  'Спасибо!'
  ]
#strings_positions = custom_write("test.txt", strings)
#print(strings_positions)
result = custom_write('test.txt', strings)
for elem in result.items():
  print(elem)
