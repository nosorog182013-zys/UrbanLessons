#2023/11/24 00:00|Домашнее задание по теме "Try и Except"
def add_everything_up(a, b):
  try:
    return round(a + b, 3)
  except TypeError:
    print(f"{a}{b}")

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

