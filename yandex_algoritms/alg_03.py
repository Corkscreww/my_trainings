'''Яндекс тренировки по алгоритмам 2021, занятие 3'''

'''A. Количество различных чисел +++'''

# with open('input.txt') as inp_file:
#     numbers = set(inp_file.read().strip().split())

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     out_file.write(str(len(numbers)))

'''B. Пересечение множеств ---'''

# with open('input.txt') as inp_file:
#     numbers1 = set(inp_file.readline().strip().split())
#     numbers2 = set(inp_file.readline().strip().split())

# result = sorted(numbers1.intersection(numbers2))

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(*result, file=out_file, end='')

'''C. Кубики'''

# with open('input.txt') as inp_file:
#     n, m = tuple(map(int, inp_file.readline().strip().split()))
#     anya = set(int(inp_file.readline().strip()) for _ in range(n))
#     borya = set(int(inp_file.readline().strip()) for _ in range(m))

# an_bor = anya.intersection(borya)
# an_un = anya - borya
# bor_un = borya - anya

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(len(an_bor), file=out_file)
#     print(*sorted(an_bor), file=out_file)
#     print(len(an_un), file=out_file)
#     print(*sorted(an_un), file=out_file)
#     print(len(bor_un), file=out_file)
#     print(*sorted(bor_un), file=out_file, end='')

'''D. Количество слов в тексте'''

# with open('input.txt') as inp_file:
#     text = set(inp_file.read().split())

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(len(text), file=out_file)

'''E. OpenCalculator +++ '''

# with open('input.txt') as inp_file:
#     btns = set(inp_file.readline().strip().split())
#     digits = set(inp_file.readline().strip())

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(len(digits.difference(btns)), file=out_file)

'''F. Инопланетный геном ---'''

# def genom_count(gen1, gen2):
#     count = 0
#     for gen in gen1:
#         if gen in gen2:
#             count += 1
#             pass
#     return count

# with open('input.txt') as inp_file:
#     gen1 = inp_file.readline().strip()
#     gen2 = inp_file.readline().strip()

# gen1 = list(gen1[i] + gen1[i+1] for i in range(len(gen1) - 1))
# gen2 = list(gen2[i] + gen2[i+1] for i in range(len(gen2) - 1))

# result = genom_count(gen1, gen2)

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(result, file=out_file)

'''G. Черепахи'''

# with open('input.txt') as inp_file:
#     n = int(inp_file.readline())

#     turtles = tuple(tuple(map(int, turtle.strip().split())) for turtle in
#                     inp_file.readlines())

# turtl_stack = set()

# for a, b in turtles:
#     if a + 1 + b == n and a + 1 not in turtl_stack:
#         turtl_stack.add(a + 1)

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(len(turtl_stack), file=out_file)

'''H. Злые свинки +++ '''

# with open('input.txt') as inp_file:
#     n = inp_file.readline()
#     shoots = len(set(tuple(map(int, bird.strip().split()))[0] for bird in
#                      inp_file.readlines()))

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(shoots, file=out_file)

'''I. Полиглоты +++ '''

# with open('input.txt') as inp_file:
#     n = inp_file.readline()
#     students = list()
#     student = list()
#     languages = set()
#     for line in inp_file.readlines():
#         line = line.strip()
#         if line.isdigit():
#             if student:
#                 students.append(student)
#             student = list()
#         else:
#             student.append(line.strip())
#             languages.add(line.strip())

# students.append(student)
# langs = set(students[0])
# for lang in students:
#     langs &= set(lang)

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(len(langs), file=out_file)
#     print(*langs, file=out_file, sep='\n')
#     print(len(languages), file=out_file)
#     print(*languages, file=out_file, sep='\n')

'''J. Пробежки по Манхеттену'''


