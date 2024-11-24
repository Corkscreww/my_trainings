'''A Кондиционер'''

# with open('input.txt', encoding='utf-8') as in_file:
#     troom, tcond = tuple(map(lambda x: int(x),
#                              in_file.readline().strip().split()))
#     mode = in_file.readline().strip()

# if mode == 'auto':
#     result = tcond
# elif mode == 'fan':
#     result = troom
# elif mode == 'freeze':
#     if troom <= tcond:
#         result = troom
#     else:
#         result = tcond
# elif mode == 'heat':
#     if troom <= tcond:
#         result = tcond
#     else:
#         result = troom

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(result, file=out_file)

''' B. Треугольник'''

# from os import chdir

# chdir('./yandex_algoritms/')

# with open('input.txt', encoding='utf-8') as in_file:
#     a = int(in_file.readline())
#     b = int(in_file.readline())
#     c = int(in_file.readline())

# solution = 'NO'
# if a < b + c and b < a + c and c < a + b:
#     solution = 'YES'

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(solution, file=out_file)

'''C. Телефонные номера'''

# from os import chdir

# chdir('./yandex_algoritms/')

# def format_number(numb):
#     lets = ['+', '-', '(', ')']
#     for let in lets:
#         numb = numb.replace(let, '')

#     if numb[0] != '7' and numb[0] != '8':
#         numb = '495' + numb
#     else:
#         numb = numb[1:]

#     return numb

# with open('input.txt', encoding='utf-8') as inp_file:
#     request = format_number(inp_file.readline().strip())
#     numbers = [format_number(num.strip()) for num in inp_file.readlines()]

# result = ''
# for num in numbers:
#     if num == request:
#         result += 'YES\n'
#     else:
#         result += 'NO\n'
#     pass

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(result, file=out_file)

'''D. Уравнение с корнем'''

# from os import chdir

# chdir('./yandex_algoritms/')

# def solution(a, b, c):
#     if c < 0:
#         return 'NO SOLUTION'

#     if a == 0:
#         return 'MANY SOLUTIONS'
    
#     x = (c ** 2 - b) // a
#     ost = (c ** 2 - b) % a
#     if ost == 0:
#         return x
#     else:
#         return 'NO SOLUTION'

# with open('input.txt', encoding='utf-8') as inp_file:
#     a, b, c = tuple(map(int, inp_file.readlines()))

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(solution(a, b, c), file=out_file)

'''E. Скорая помощь'''

# from os import chdir

# chdir('./yandex_algoritms/')

# with open('input.txt', encoding='utf-8') as inp_file:
#     k1, m, k2, p2, n2 = tuple(map(int, inp_file.read()))


# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(solution(a, b, c), file=out_file)

'''F. Расстановка ноутбуков'''

# from os import chdir

# chdir('./yandex_algoritms/')

# with open('input.txt', encoding='utf-8') as inp_file:
#     inp = inp_file.read().strip().split()
#     a1, b1, a2, b2 = tuple(map(int, inp))

# squares = []
# amin = a1 + a2
# bmin = max(b1, b2)
# square_min = amin * bmin

# a = a1 + b2
# b = max(b1, a2)
# square = a * b
# if square < square_min:
#     amin, bmin, square_min = a, b, square

# a = b1 + b2
# b = max(a1, a2)
# square = a * b
# if square < square_min:
#     amin, bmin, square_min = a, b, square

# a = b1 + a2
# b = max(a1, b2)
# square = a * b
# if square < square_min:
#     amin, bmin, square_min = a, b, square

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(*(amin, bmin), file=out_file)

'''G. Детали'''

# from time import perf_counter

# start_input = perf_counter()
# with open('input.txt', encoding='utf-8') as inp_file:
#     inp = inp_file.read().strip().split()
#     n, k, m = tuple(map(int, inp))
# print(f'Время импортирования входных данных: {perf_counter() - start_input}')

# start = perf_counter()
# part_count = 0
# while n >= k:
#     blank_residue = n % k
#     blank_amount = n // k
#     if blank_amount > 0:
#         part_amount = (k // m) * blank_amount
#         part_count += part_amount
#         part_residue = (k % m) * blank_amount
#         pass
#     n = blank_residue + part_residue
#     pass
# print(f'Время выполнения программы: {perf_counter() - start}')


# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(part_count, file=out_file)

'''H. Метро'''

# def time_calc(interval, count):
#     t_min = (interval + 1) * (count - 1) + 1
#     t_max = (interval + 1) * count + 1
#     time = set(range(t_min, t_max + 1))
#     return time

# with open('input.txt', encoding='utf-8') as inp_file:
#     a, b, n, m = tuple(map(int, inp_file.read().split()))

# result_time = time_calc(a, n).intersection(time_calc(b, m))

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     if result_time:
#         time = (min(result_time), max(result_time))
#         print(*time, file=out_file)
#     else:
#         print(-1, file=out_file)

'''Узник замка ИФ'''

# with open('input.txt', encoding='utf-8') as inp_file:
#     inp = inp_file.read().strip().split()
#     a, b, c, d, e = tuple(map(int, inp))

# opt = list(map(sorted, [[a, b], [a, c], [b, c]]))
# hole = sorted([d, e])

# answer = 'YES' if any(
#         map(lambda x: x[0] <= hole[0] and x[1] <= hole[1], opt)) else 'NO'

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(answer, file=out_file)

'''J. Система линейных уравнений - 2'''


