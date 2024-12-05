#2023/11/29 00:00|Домашнее задание по теме "Введение в функциональное программирование"
def apply_all_func(int_list, *functions):
  results = {}
  for function in functions:
    function_name = function.__name__
    results[function_name] = function(int_list)
  return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

