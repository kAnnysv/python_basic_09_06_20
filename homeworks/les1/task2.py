user_answer = input('Введите количество секунд: ')
user_answer = int(user_answer)
hour = (user_answer // 3600)
min = (user_answer - (hour * 3600)) // 60
sec = (user_answer - (hour * 3600) - (min * 60)) / 60
round(sec, 1)
print(f'{hour} часов {min} минут {sec}секунд')
