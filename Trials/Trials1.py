salaries = [500, 600, 800, 850, 900]
names = ['Tom', 'Mark', 'Jane', 'Helen', 'Izzy']
salaries_by_names = zip(names, salaries)
print(salaries_by_names)
print(list(salaries_by_names))
queries_string = "танго, парный танец, танец танго, занятия танго, музыка танго"
# преобразуем строку в список
queries_list = queries_string .split(",")
print(queries_list)
'танго' in queries_list
print('танго' in queries_list)
