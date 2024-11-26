'''Тренировки по алгоритмам, занятие 2'''

'''A. Возрастает ли список?'''

# def solution(seq):
#     if seq:
#         if len(seq) == 1:
#             return 'YES'
#         for i in range(len(seq) - 1):
#             tek = seq[i]
#             sled = seq[i + 1]
#             if seq[i] >= seq[i + 1]:
#                 return 'NO'
#         return 'YES'

# with open('input.txt') as inp_file:
#     data = list(map(int, inp_file.read().split()))

# pass
# ans = solution(data)
# pass

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(solution(data), file=out_file)

'''B. Определить вид последовательности'''

# def cons(seq):
#     return all(map(lambda x: x == seq[0], seq))

# def asc(seq):
#     for i in range(len(seq) - 1):
#         if seq[i] >= seq[i + 1]:
#             return False
#     return True

# def wasc(seq):
#     for i in range(len(seq) - 1):
#         if seq[i] > seq[i + 1]:
#             return False
#     return True

# def desc(seq):
#     for i in range(len(seq) - 1):
#         if seq[i] <= seq[i + 1]:
#             return False
#     return True

# def wdesc(seq):
#     for i in range(len(seq) - 1):
#         if seq[i] < seq[i + 1]:
#             return False
#     return True

# def deter(seq):
#     RESULT = {
#             0: 'CONSTANT',
#             1: 'ASCENDING',
#             2: 'WEAKLY ASCENDING',
#             3: 'DESCENDING',
#             4: 'WEAKLY DESCENDING',
#             5: 'RANDOM',
#     }

#     seq = seq[:seq.index(-2000000000)]

#     if cons(seq):
#         return RESULT[0]
#     if asc(seq):
#         return RESULT[1]
#     if wasc(seq):
#         return RESULT[2]
#     if desc(seq):
#         return RESULT[3]
#     if wdesc(seq):
#         return RESULT[4]

#     return RESULT[5]

# with open('input.txt', encoding='utf-8') as inp_f:
#     seq = list(map(int, inp_f.readlines()))

# with open('output.txt', 'w', encoding='utf-8') as out_f:
#     print(deter(seq), file=out_f)

'''C. Ближайшее число'''

# def minimum_dif(seq, numb):
#     min_dif = sorted(list(map(lambda x: abs(numb - x), seq)))[0]
#     val1 = numb - min_dif
#     val2 = numb + min_dif
#     result = val1 if val1 in seq else val2
#     return result

# with open('input.txt', encoding='utf-8') as inp_file:
#     inp_file.readline()
#     seq = list(map(int, inp_file.readline().strip().split()))
#     numb = int(inp_file.readline())

# with open('output.txt', 'w', encoding='utf-8') as out_f:
#     print(minimum_dif(seq, numb), file=out_f)

'''D. Больше своих соседей'''

# def neigh_emount(seq):
#     count = 0
#     for i in range(1, len(seq) - 1):
#         if seq[i] > seq[i - 1] and seq[i] > seq[i + 1]:
#             count += 1
#     return count

# with open('input.txt', encoding='utf-8') as inp_file:
#     seq = list(map(int, inp_file.read().strip().split()))

# with open('output.txt', 'w', encoding='utf-8') as out_f:
#     print(neigh_emount(seq), file=out_f)

'''E. Чемпионат по метанию коровьих лепёшек'''

pass

'''G. Наибольшее произведение двух чисел'''

# def result(seq):
#     seq.sort()
#     result = (seq[:2]) + (seq[-2:])
#     return seq[:2] if seq[0] * seq[1] > seq[-2] * seq[-1] else seq[-2:]

# with open('input.txt', encoding='utf-8') as inp_file:
#     seq = list(map(int, inp_file.read().strip().split()))

# pass

# with open('output.txt', 'w', encoding='utf-8') as out_f:
#     print(*result(seq), file=out_f)

'''H. Наибольшее произведение трех чисел'''

# def result(seq):
#     seq.sort()
#     result = (seq[:3]) + (seq[-3:])
#     return (
#         seq[:3]
#         if seq[0] * seq[1] * seq[2] > seq[-3] * seq[-2] * seq[-1]
#         else seq[-3:]
#     )

# with open('input.txt', encoding='utf-8') as inp_file:
#     seq = list(map(int, inp_file.read().strip().split()))

# pass

# with open('output.txt', 'w', encoding='utf-8') as out_f:
#     print(*result(seq), file=out_f)

'''I. Сапер'''

# def field_create(field, mines):
#     field = [[0 for _ in range(field[1])] for _ in range(field[0])]
#     for i, j in mines:
#         field[i - 1][j - 1] = '*'
#         pass
#     return field

# def coord_check(i, j, field):
#     if i < 0 or j < 0 or i == len(field) or j == len(field[0]):
#         return True

# def field_mins_count(field):
#     coord_dpl = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
#                  (1, 1))

#     for i in range(len(field)):
#         for j in range(len(field[0])):
#             if field[i][j] != '*':
#                 count = 0
#                 for x, y in coord_dpl:
#                     di, dj = i, j
#                     di += x
#                     dj += y
#                     if coord_check(di, dj, field):
#                         continue
                    
#                     if field[di][dj] == '*':
#                         count += 1
#                 field[i][j] = count
#     return field

# with open('input.txt', encoding='utf-8') as inp_file:
#     field = tuple(map(int, inp_file.readline().strip().split()))
#     mines = tuple(tuple(map(int, row.strip().split())) for row in
#                   inp_file.readlines())

# field = field_create(field, mines)
# field = field_mins_count(field)

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     for row in field:
#         print(*row, file=out_file)

'''J. Треугольник Максима'''


