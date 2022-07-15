num_boy = int(input('Загадайте число: '))
min_limit = 1
max_limit = 100
attempt = 0
while True:
  num = (min_limit + max_limit) // 2
  answ = int(input('Твое число равно, меньше или больше, чем число ' + str(num) + '? (1 - равно; 2 - больше; 3 - меньше) '))
  if answ == 1:
    print('Ура! Я угадал!')
    break
  elif answ == 2:
    min_limit = num + 1
  elif answ == 3:
    max_limit = num - 1
  attempt += 1
print('Количество попыток:', attempt)