'''Поколение Python: квесты, конкурсы, марафоны, тесты, задачи'''

'''2 Квест на миллион'''

'''2.1 Гвидо рассуждает с экрана терминала:

    — Люди постоянно тратят время на игры, результат которых зависит только от
    удачи. Подумать только, по доброй воле спускать деньги в казино! Мы, роботы,
    гораздо практичнее. Давай сыграем в следующую игру. Я загадал 
    4
    4 различных положительных целых числа A, B, C, D, при этом A < B < C < D. Я
    называю 
    8
    8 чисел в произвольном порядке: A, B, C, D, A × B, B × C, C × D, D × A. Твоя
    задача — найти число D. Справишься или предпочтешь игру попроще? Могу
    принести футбольный мячик. ⚽

    Задание нужно выполнить в виде программы, которая получает на вход числа A,
    B, C, D, A × B, B × C, C × D, D × A (на одной строке) согласно условию.
    Программа должна вывести одно число D.

    Примечание. Считайте, что числа A, B, C, D, A × B, B × C, C × D, D × A не
    превосходят 
    2
    63
    −
    1
    2 
    63
     −1.

     Ограничения
     Sample Input 1:

     2 3 4 1 12 6 2 4
     Sample Output 1:

     4
     Sample Input 2:

     2 6 7 3 14 35 15 5
     Sample Output 2:

    7
     Sample Input 3:

     1971 78 7644 98 27 5694 73 2646
     Sample Output 3:

     98
     Sample Input 4:

     54 979 242 22 11 89 1188 4806
     Sample Output 4:

     89
     Sample Input 5:

     50505987 20437483 39174299 482997400740360 925803074323080 1032215250710721
     1978536636028113 23632920
     Sample Output 5:

     50505987
     Sample Input 6:

     644047902489600 555893253563820 1266753284294400 30973035 1093365263588355
     35300553 17947652 35884800
     Sample Output 6:

     35884800
     Sample Input 7:

     20 10 6 5 4 3 2 12
     Sample Output 7:

     5
     Sample Input 8:

     2 6 18 3 6 7 42 14
     Sample Output 8:

     7
     Sample Input 9:

     7 96 8 240 12 140 20 56
     Sample Output 9:

     20
     Sample Input 10:

     20 30 6 7 4 42 28 5
     Sample Output 10:

     7
     Sample Input 11:

     2 6 12 3 20 4 5 10
     Sample Output 11:

     5
     Sample Input 12:

     2 5 20 21 10 100 420 42
     Sample Output 12:

     21
     Sample Input 13:

     7 217 15 589 31 105 19 285
     Sample Output 13:

     31
     Sample Input 14:

     49 1840 294 6 40 240 46 2254
     Sample Output 14:

     49
     Sample Input 15:

     240 24 10 9 468 1248 90 52
     Sample Output 15:

     52

'''

from random import shuffle, sample, choice
from copy import deepcopy
from time import perf_counter

def check(numb):
    a, b, c, d, ab, bc, cd, da = numb
    # print('проверяем')
    # if (
    #         a * b == ab
    #         and b * c == bc
    #         and c * d == cd
    #         and d * a == da
    #         and a < b < c < d
    # ):
    if a * b == ab:
        # if b * c == bc:
        if c * d == cd:
            # if d * a == da:
            if a < b < c < d:
                print('ЗАЕБИСЬ!!!')
                print(f'a = {a}\n'
                      f'b = {b}\n'
                      f'c = {c}\n'
                      f'd = {d}\n'
                      f'ab = {ab}\n'
                      f'bc = {bc}\n'
                      f'cd = {cd}\n'
                      f'da = {da}\n')
                return (a, b, c, d, ab, bc, cd, da)
    # print('нихуя')
    return False

program_time = perf_counter()

time_open_file = perf_counter()
with open('input.txt', encoding='utf-8') as inp_file:
    numbers = list(map(int, inp_file.readline().strip().split()))
time_open_file -= perf_counter()

print(f'Время импортирования данных из файла: {abs(time_open_file)}')

deepcopy_count, shuffle_count, check_count, k, l  = 0, 0, 0, 0, 0
copy_time, copy_count, deep_copy_time, shuffle_time, check_time = 0, 1, 0, 0, 0
cash = []
answer = False
while not answer:
    # start = perf_counter()
    # nums = deepcopy(numbers)
    # deep_copy_time += perf_counter() - start
    # deepcopy_count += 1

    start = perf_counter()
    nums = sample(numbers, 8)
    # nums = [num for num in numbers
    # copy_time += perf_counter() - start
    # copy_count += 1

    # start = perf_counter()
    # shuffle(nums)
    shuffle_time += perf_counter() - start
    shuffle_count += 1

    l += 1
    # print('перемешали')
    if nums not in cash:
        cash.append(nums)
        # print('такого еще не пробовали, добавляем')
        start = perf_counter()
        answer = check(nums)
        check_time += perf_counter() - start
        check_count += 1
    else:
        k += 1

percent = round((k / l) * 100, 2)
print(f'{l} попыток, {k} совпадений - {100 - percent} %')
# print(f'deepcopy {deepcopy_count} times, {deep_copy_time} sec., '
#       f'{deep_copy_time / deepcopy_count} sec/time')
print(f'shuffle {shuffle_count} times, {shuffle_time} sec., '
              f'{shuffle_time / shuffle_count} sec/time')
print(f'check {check_count} times, {check_time} sec., '
            f'{check_time / check_count} sec/time')
print(f'copy {copy_count} times, {copy_time} sec., '
            f'{copy_time / copy_count} sec/time')

program_time -= perf_counter()
print(f'TOTAL TIME: {abs(program_time)}')

with open('output.txt', 'a', encoding='utf-8') as out_file:
    print(f'a = {answer[0]}\n'
          f'b = {answer[1]}\n'
          f'c = {answer[2]}\n'
          f'd = {answer[3]}\n'
          f'ab = {answer[4]}\n'
          f'bc = {answer[5]}\n'
          f'cd = {answer[6]}\n'
          f'da = {answer[7]}\n', file=out_file)
    print(f'{l} попыток, {k} совпадений - {100 - percent} %', file=out_file)
    # print(f'deepcopy {deepcopy_count} times, {deep_copy_time} sec., '
    #       f'{deep_copy_time / deepcopy_count} sec/time')
    print(f'shuffle {shuffle_count} times, {shuffle_time} sec., '
                  f'{shuffle_time / shuffle_count} sec/time', file=out_file)
    print(f'check {check_count} times, {check_time} sec., '
                f'{check_time / check_count} sec/time', file=out_file)
    print(f'copy {copy_count} times, {copy_time} sec., '
                f'{copy_time / copy_count} sec/time', file=out_file)
    print(f'-------------------------------------------', file=out_file)
    print(f'TOTAL_TIME: {abs(program_time)}\n', file=out_file)

