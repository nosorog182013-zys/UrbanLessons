def custom_write(file_name, strings):
  """
  Записывает в файл file_name все строки из списка strings, каждая на новой строке.
  Возвращает словарь strings_positions, где ключом будет кортеж 
  (<номер строки>, <байт начала строки>), а значением - записываемая строка.
  """
  strings_positions = {}
  with open(file_name, "w") as f:
    for i, string in enumerate(strings):
      f.write(string + "\n")
      # Получаем текущую позицию файла
      current_position = f.tell()
      # Находим позицию начала текущей строки, отнимая длину текущей строки и символа новой строки
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

