'''B. Через тернии к клиенту'''

# Извлекаем из файла с входными данными все записи, разбиваем на списки по
# каждой записи, и каждую запись разбиваем на списки по конкретным значениям
with open('input.txt', encoding='utf-8') as input_file:
    p = input_file.readline()
    input_data = [
            record.split() for record in
            list(map(str.strip, input_file.readlines()))
    ]
    input_data = list(map(
        lambda x: [int(x[i]) for i in range(4)] + list(x[4]), input_data
        ))

# Получаем список кораблей
ships = list(set([int(record[3]) for record in input_data]))
ships.sort()

ships_data = {} # Словарь формата {<id корабря>: [список записей по коралю id]}

# Заполняем словарь данных по каждому кораблю,
# обрезая id корабля из каждой записи
for ship in ships:
    ships_data[ship] = [
            list(map(
                lambda rec: rec[:3] + rec[4:],
                filter(lambda n: n[3] == ship, input_data)
                ))
    ]

for ship in ships_data:
    data = ships_data[ship]
    pass
    data.sort(key=data.sort(key=data.sort(key=data[2])[1])[0])

pass
