
import random


def guess():
    x = 0
    y = 100
    tries_numbers = 0
    with open("finaly.txt", "w",) as f:
        assumption = random.randint(x, y)
        while True:
            tries_numbers += 1
            print(f"Предполагаемое число: {assumption}")
            response = input(
                "Да ты угадал, Мое число больше или  Мое число меньше?").lower()
            if response == "да ты угадал":
                f.write(f"Количество попыток: {tries_numbers}\n")
                f.write(f"Список попыток: {assumption}\n")
                f.write(f"Загаданное число: {assumption}\n")
                break
            elif response == "Мое число меньше":
                max_num = assumption - 1
            elif response == "Мое число больше":
                min_num = assumption + 1
            else:
                print(
                    "Пожалуйста, введите 'да ты угадал', Мое число больше или Мое число меньше")
                continue
            assumption = random.randint(min_num, max_num)


guess()

# import random
# number = int(input("Введите число от 0 до 100: "))

# x = 0
# y = 100
# guess = random.randint(x, y)
# tries = 1

# if number == guess:
#     print('С первой попытки!')
# else:
#     while guess != number:
#         if number > guess:
#             print("Загаданное число больше: ", guess)
#             x = guess
#             guess = random.randint(x, y)
#             tries += 1
#         elif number < guess:
#             print("Загаданное число меньше: ", guess)
#             y = guess
#             guess = random.randint(x, y)
#             tries += 1
#     print(number)


# #     print('В яблочко, с', tries, 'попытки')
