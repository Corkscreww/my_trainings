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

