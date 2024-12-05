#2023/11/30 00:00|Домашнее задание по теме "Списковые, словарные сборки"
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
all_strings = first_strings + second_strings

first_result = [len(first_string) for first_string in first_strings if len(first_string) > 5]

second_result = [(first_string, second_string) for first_string in first_strings for second_string in second_strings if len(first_string) == len(second_string)]

third_result = {all_string: len(all_string) for all_string in all_strings if len(all_string) // 2}

print(first_result)
print(second_result)
print(third_result)
