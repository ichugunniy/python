from random import *

print(
    "Добро пожаловать в числовую угадайку! Давайте угадаем загаданное число от 1 до 100!"
)
count_try = 5
goal_dig = randint(1, 100)
low = 1
high = 100
for i in range(count_try, 0, -1):
    if i == 1:
        print("У вас 1 попытка:")
    elif i == 0:
        print("У вас 0 попыток.")
        print("ВЫ ИСПОЛЬЗОВАЛИ ВСЕ ПОПЫТКИ!")
        print("ПОПРОБУЙТЕ СНОВА! ПРОСТО НАЖМИТЕ RUN!")
        break
    else:
        print("У вас", i, "попытки:")

    your_dig = int(input())

    while your_dig < low or your_dig > high:
        print("Данное число не входит в последовательность!")
        print("Введите число заново!")
        your_dig = int(input())
    if goal_dig == your_dig:
        print("Вы угадали число!")
        break
    elif goal_dig > your_dig:
        print("Вы не угадали число(")
        print("Ваше число меньше")
        low = your_dig
    elif goal_dig < your_dig:
        print("Вы не угадали число")
        print("Выше число больше")
        high = your_dig
    else:
        print("Вы не угадали число(")
        print("Попробуйте еще раз!")
