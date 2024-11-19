'''А. Хитрый шифр'''

# def get_input_data():
#     with open('input.txt', encoding='UTF-8') as input_file:
#         data = []
#         N = int(input_file.readline())
#         for i in input_file:
#             data.append(i.strip())
#     return data

# def put_output_data(result):
#     with open('output.txt', 'w', encoding='UTF-8') as output_file:
#         output_file.write(' '.join(result))

# data = get_input_data()
# result = []
# # Проходим циклом по всем участникам
# for man in data:
#     # Сначала извлекаем все данные участника
#     f, i, o, d, m, y = man.split(',')

#     # затем подсчитываем клдичество различных символов в ФИО
#     symb = set(list(f) + list(i) + list(o))
#     symb = len(symb)

#     # затем вычисляем сумму всех цифр в дате рождения
#     summ = list(d)
#     summ.append(m)
#     summ = sum(map(int, summ)) * 64

#     # После этого определяем номер первлй буквы фамилии и умноэаем на 256
#     num_first_family_char = f[0]
#     if num_first_family_char.islower():
#         num_first_family_char = ord(num_first_family_char) - 96
#     else:
#         num_first_family_char = ord(num_first_family_char) - 64

#     num_first_family_char *= 256

#     summa = symb + summ + num_first_family_char

#     summa = hex(summa)
#     summa = summa[summa.find('x') + 1:]
#     if len(summa) < 3:
#         summa = '0' * (3 - len(summa)) + summa
#     else:
#         summa = summa[-3 :].upper()
#     # summ_bd = sum(map(int, (list(d).extend(d).extemd(y))))
#     print(summa)
#     result.append(summa)

# put_output_data(result)

