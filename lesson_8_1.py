# работа с файлами
# w - write
# a - add
# x - create without deleting data
# r - read
# from random import choice

# with open('results.txt', 'w') as new:
#     new.write('results for 29-1'.upper())

# students = [8, 6, 12, 13, 4, 9, 1, 17, 11, 14, 16, 20, 3, 19, 7, 2, 5]

# while len(students) > 0:
#     print(f'in students list... {len(students)}')
#     student_id = choice(students)
#     name = input(f'name for {student_id}: ').title()
#     try:
#         rate = int(input(f'rate for {name}: '))
#         with open('results.txt', 'a') as file:
#             file.write(f'\n{name}: {rate}')
#         students.remove(student_id)
#     except:
#         print('wrong rate, must be integer!')









from time import sleep

with open('file.txt', 'r') as new:
    print(new.readlines())
    print(new.read())
    for i in new.read().split(' '):
        print(i, end=' ')
        sleep(1)


# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан!')
# file.close()

# with open('file1.txt', 'x') as file:
#     file.write('new string!')

# with open('file1.txt', 'a') as file:
#     file.write('new string!')


