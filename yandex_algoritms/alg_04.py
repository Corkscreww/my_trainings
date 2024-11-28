''' Яндекс. Тренировки по алгоритмам, занятие 4'''

'''A. Словарь синонимов'''

# with open('input.txt', encoding='utf-8') as inp_file:
#     n = int(inp_file.readline().strip())
#     data = {}
#     for i in range(n):
#         synonym, word = tuple(inp_file.readline().strip().split())
#         data[word] = synonym
#         data[synonym] = word
#     word = inp_file.readline().strip()

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(data[word], file=out_file)

'''B. Номер появления слова'''

# with open('input.txt', encoding='utf-8') as inp_file, open(
#             'output.txt', 'w', encoding='utf-8') as out_file:
#     result_dict = {}
#     for word in inp_file.read().strip() .split():
#         result_dict.setdefault(word, 0)
#         print(result_dict[word], file=out_file, end=' ')
#         result_dict[word] += 1

'''C. Самое частое слово'''

# with open('input.txt', encoding='utf-8') as inp_file:
#     text = inp_file.read().strip().split()

# words = {}
# for word in text:
#     words.setdefault(word, 0)
#     words[word] += 1

# result = list(filter(lambda x: words[x] == max(words.values()), words))
# result.sort()

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(result[0], file=out_file)

'''D. Клавиатура'''

# with open('input.txt') as inp_file:
#     n = int(inp_file.readline().strip())
#     vls = map(int, inp_file.readline().strip().split())
#     inp_file.readline()
#     presses = map(int, inp_file.readline().strip().split())

# keyboard = {}
# for i in range(1, n + 1):
#     keyboard[i] = next(vls)

# for press in presses:
#     keyboard[press] -= 1

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     for key in keyboard:
#         result = 'YES' if keyboard[key] < 0 else 'NO'
#         print(result, file=out_file)

'''E. Пирамида'''

# with open('input.txt') as inp_file:
#     n = int(inp_file.readline().strip())
#     blks = [map(int, line.strip().split()) for line in inp_file]

# blocks = {}
# for w, h in blks:
#     blocks.setdefault(w, [])
#     blocks[w].append(h)

# max_heigh = 0
# for block in blocks:
#     max_heigh += max(blocks[block])

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     print(max_heigh, file=out_file)

'''F. Продажи'''

# with open('input.txt', encoding='utf-8') as inp_file:
#     check = {}
#     for purchase in inp_file.readlines():
#         name, item, amount = purchase.strip().split()
#         check.setdefault(name, {})
#         check[name].setdefault(item, 0)
#         check[name][item] += int(amount)

# with open('output.txt', 'w', encoding='utf-8') as out_file:
#     for buyer in sorted(check):
#         print(f'{buyer}:', file=out_file)
#         for product in sorted(check[buyer]):
#             print(f'{product} {check[buyer][product]}', file=out_file)

'''G. Банковские счета'''

# def deposit(data):
#     name = data[0]
#     amount = int(data[1])
#     bank.setdefault(name, 0)
#     bank[name] += amount

# def withdraw(data):
#     name = data[0]
#     amount = int(data[1])
#     bank.setdefault(name, 0)
#     bank[name] -= amount

# def income(percent):
#     percent = int(percent[0])
#     for name in bank:
#         bank[name] += int(bank[name] * percent / 100)

# def transfer(data):
#     name_transmitter = data[0]
#     name_reciever = data[1]
#     amount = int(data[2])
#     bank.setdefault(name_transmitter, 0)
#     bank.setdefault(name_reciever, 0)
#     bank[name_transmitter] -= amount
#     bank[name_reciever] += amount

# def balance(name):
#     name = name[0]
#     if name not in bank:
#         print('ERROR', file=out_file)
#     else:
#         print(bank[name], file=out_file)

# operations = {
#         'DEPOSIT': deposit,
#         'WITHDRAW': withdraw,
#         'INCOME': income,
#         'TRANSFER': transfer,
#         'BALANCE': balance
# }

# bank = {}
# with (
#         open('input.txt', encoding='utf-8') as inp_file,
#         open('output.txt', 'w', encoding='utf-8') as out_file
# ):

#     for operation in inp_file:
#         operation = operation.strip().split()
#         operation_name, data = operation[0], operation[1:]
#         operations[operation_name](data)

'''H. Расшифровка письменности Майя'''


