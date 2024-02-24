"""
Создать функцию вычисления факториала числа.
Функция принимает в качестве аргумента число, возвращает его факториал.
"""
from random import randint


def func_1_factorial(number: int) -> int | float:
    start = 1
    result = 1
    for i in range(number):
        result = result * start
        start += 1
    return result


def func_2_max_number(*args) -> int | float:
    max_ = 0
    for i in args:
        if i > max_:
            max_ = i
    return max_


def func_3_triangle_square(leg_1: int, leg_2: int) -> int | float:
    return (leg_1 * leg_2) / 2


def task_1():
    a, b, c = 15, randint(1, 99), randint(1, 99)
    print(f"Факториал числа a({a}) - {func_1_factorial(a)}")
    print(f"Из чисел a = {a}, b = {b}, c = {c} самое большое - {func_2_max_number(a, b, c)}")
    print(f"Из чисел a = {a}, b = {b}, c = {c} самое большое - {max((a, b, c))}")
    print(f"Катет a = {a} см, катет b = {b} см, площадь треугольника равна - {func_3_triangle_square(a, b)}")
    """
    Создайте функцию для генерации текста с адресом суда.
Функция должна по шаблону генерировать шапку для процессуальных документов с
реквизитами сторон для отправки.

Пример работы функции:
В арбитражный суд города Москвы
Адрес: 115225, г. Москва, ул. Б. Тульская, 17
Истец: Пупкин Василий Геннадьевич
ИНН 1236182357 ОГРНИП 218431927812733
Адрес: 123534, г. Москва, ул. Опущенных водников, 13
Ответчик: ООО “Кооператив Озеро”
ИНН 1231231231 ОГРН 123124129312941
Адрес: 123534, г. Москва, ул. Красивых молдавских партизан, 69
Номер дела А40-123456/2023
"""


def make_court_nominative_case(court_name: str) -> str:
    """

    :param court_name:
    :return:
    """
    words = court_name.split(" ")[2::]
    text = "Арбитражный суд"
    for i in words:
        text += f" {i}"
    return text


def make_a_header(court, plaintiff, respondent):
    text = f"-------------------------------\n" \
           f"В {make_court_nominative_case(court['court_name'])}\n" \
           f"Адрес: {court['court_address']}\n\n" \
           f"" \
           f"Истец: {plaintiff['name']}" \
           f"ИНН {plaintiff['inn']} ОГРНИП {plaintiff['ogrnip']}\n" \
           f"Адрес: {plaintiff['address']}\n\n" \
           f"" \
           f"Ответчик: {respondent['short_name']}”\n" \
           f"ИНН {respondent['inn']} ОГРН {respondent['ogrn']}\n" \
           f"Адрес: {respondent['address']}\n\n" \
           f"" \
           f"Номер дела {respondent['case_number']}\n"
    return text


def task_2():
    plaintiff = {
        "name": "Сиротинский Кирилл Александрович",
        "inn": "1236182357",
        "ogrnip": "218431927812733",
        "address": "123534, г. Москва, ул. Красивых молдавских партизан, 69"
    }
    cleaned_respondents = [i for i in respondents if i.get("case_number")]
    for respondent in cleaned_respondents:
        court_code = respondent["case_number"].split("-")[0]
        court = courts[court_code]
        result = make_a_header(court, plaintiff, respondent)
        print(result)
"""
Напишите функцию для валидации ИНН (идентификационного номера
налогоплательщика), которая принимает в качестве аргумента строку, содержащую
ИНН или просто набор цифр, похожий на ИНН.

Функция возвращает True в случае, если ИНН прошёл проверку, и False, если проверка
не пройдена.
    """
def is_org_inn(inn: str):
    numbers = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    check_sum = 0
    for i, number in enumerate(numbers):
        check_sum = check_sum + (int(inn[i]) * number)
    check_number = check_sum % 11
    if check_number > 9:
        check_number = check_number % 10
    if check_number == int(inn[-1]):
        return True
    else:
        return False


my_inn = "263411857320"


def is_person_inn(inn: str):
    k_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    k_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    sum_1 = 0
    sum_2 = 0
    for i, c in enumerate(inn):
        if i > 9:
            break
        sum_1 += (int(c) * k_1[i])
    sum_1 = sum_1 % 11
    if sum_1 > 9:
        sum_1 = sum_1 % 10
    for i, c in enumerate(inn):
        if i > 10:
            break
        sum_2 += (int(c) * k_2[i])
    sum_2 = sum_2 % 11
    if sum_2 > 9:
        sum_2 = sum_2 % 10
    pass


def is_valid_inn(inn: str):
    if inn.isdigit() and len(inn) == 12:
        return is_person_inn(inn)
    elif inn.isdigit() and len(inn) == 10:
        return is_org_inn(inn)
    else:
        raise TypeError


def task_3():

    print(is_valid_inn(my_inn))


def main():
    # task_1()
    # task_2()
    task_3()


if __name__ == "__main__":
    main()
    print("stop")