#Домашнее задание по теме "Форматирование строк".
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

def tasks_total():
  return score_1 + score_2

def time_avg():
  return round((team1_time + team2_time) / tasks_total(), 1)
  
def challenge_result():
  if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды %s !" % team1
  elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды %s !" % team2
  else:
    result = "Ничья!"
  return result

print('В команде %s участников: %s !' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % ((team1_num), (team2_num)))
print('Команда {} решила задач: {} !'.format(team2, score_2))
print('{} решили задачи за {} c !'.format(team2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Всего команды решили {tasks_total()} задач.')
print(f'Среднее время на задачу: {time_avg()} c !')
print(challenge_result())
