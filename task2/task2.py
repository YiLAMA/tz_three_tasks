import requests
from bs4 import BeautifulSoup
# import csv
import json
import time

BASE_URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

HOST = 'https://ru.wikipedia.org/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/83.0.4103.116 Chrome/83.0.4103.116 Safari/537.36'}


def get_html_content(html, params=None):
    full_page = requests.get(html, headers=HEADERS, params=params)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    return soup


def get_next_page(html):
    """
    Получить следующую страницу.
    Если нет следующей страницы, то верёт None.
    """
    full_page = requests.get(html, headers=HEADERS)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # elem = soup.select('#mw-pages > a:nth-child(4)')
    elem = soup.find_all("a", {'title': 'Категория:Животные по алфавиту', })
    for e in elem:
        if e.text == "Следующая страница":
            next_page = HOST + e.attrs["href"]
            return next_page


def get_list_pages(html):
    """
    Получить список всех страниц.
    html - это обязательно первая страница
    """
    pagination = [html, ]
    while True:
        next_page = get_next_page(pagination[-1])
        if not next_page:
            break
        pagination.append(next_page)
    return pagination


def get_dict_animal(page):
    """
    Получить словарь с именами животных из конкретной страницы page.
    Словарь = { "Первая буква" : [Список всех имён начинающиеся с этой первой буквы], ...}.
    """
    dict_animal = {}
    full_page = requests.get(page, headers=HEADERS)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    elem = soup.select('#mw-pages > div > div > div > ul > li > a')
    print(elem)
    try:
        for e in elem:
            name_animal = e.attrs["title"]
            first_sym = name_animal[0]
            if first_sym not in dict_animal.keys():
                dict_animal[first_sym] = []
            if first_sym in dict_animal.keys():
                dict_animal[first_sym].append(name_animal)
            print(name_animal)
    except AttributeError:
        pass
    return dict_animal


def get_dict_all_animal(all_page):
    """
    Получить словарь с именами всех животных из списка всех страниц (животных по алфавиту).
    all_page - список из всех страниц.
    Словарь = { "Первая буква" : [Список всех имён начинающиеся с этой первой буквы], ...}.
    """
    dict_animal = {}
    for page in all_page:
        print(page)
        full_page = requests.get(page, headers=HEADERS)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        # elem = soup.find('div', {'id': 'mw-pages'}).find('ul').find_all('a')
        elem = soup.select('#mw-pages > div > div > div > ul > li > a')
        if elem == []:
            elem = soup.select('#mw-pages > div > ul > li > a')
        for e in elem:
            name_animal = e.attrs["title"]
            first_sym = name_animal[0]
            if first_sym not in dict_animal.keys():
                dict_animal[first_sym] = []
            dict_animal[first_sym].append(name_animal)
            # print(name_animal)

    return dict_animal


# def save_list_csv(list_, path):
#     """Сохранить список в файл .csv"""
#     with open(f'{path}.csv', 'w', newline='') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         for l in list_:
#             csv_writer.writerow([l])


# def get_list_csv(path):
#     """Получить список из файла (path) .csv"""
#     with open(f'{path}.csv', newline='') as f:
#         reader = csv.reader(f)
#         list_csv = list(reader)
#     return list_csv


def save_dict_json(dict_, path):
    """Сохранить словарь в файл .json"""
    with open(f'{path}.json', 'w') as f:
        f.write(json.dumps(dict_, indent=3, ensure_ascii=False))


def get_dict_json(path):
    with open(f'{path}.json', 'r', encoding='utf-8') as f:
        dict_ = json.load(f)
    return dict_


def save_list_txt(list_, path):
    """Сохранить список в файл .txt"""
    with open(f'{path}.txt', 'w') as f:
        for l in list_:
            f.write(l + '\n')


def get_list_txt(path):
    """Получить список из файла (path) .txt"""
    list_ = []
    with open(f'{path}.txt', encoding='utf-8') as f:
        for next_page in f.readlines():
            list_.append(next_page)
    return list_


def parser():
    dict_animal = {}

    # with open('list_pages_line.txt', encoding='utf-8') as f:
    #     for next_page in f.readlines():

    # list_pages = (page for page in get_list_txt('list_pages_line'))

    # list_pages = (page for page in get_list_pages(BASE_URL))
    # print(type(list_pages))
    # for next_page in list_pages:

    active_page = BASE_URL
    while True:
        print(active_page)
        # full_page = requests.get(active_page, headers=HEADERS)
        # soup = BeautifulSoup(full_page.content, 'html.parser')
        soup = get_html_content(active_page)
        elem = soup.select('#mw-pages > div > div > div > ul > li > a')
        if elem == []:
            elem = soup.select('#mw-pages > div > ul > li > a')
        for e in elem:
            name_animal = e.attrs["title"]
            first_sym = name_animal[0]
            if first_sym not in dict_animal.keys():
                dict_animal[first_sym] = []
            dict_animal[first_sym].append(name_animal)

        next_page = get_next_page(active_page)
        if not next_page:
            break
        active_page = next_page

    # Обычный вывод решения (ответа) по условиям задачки
    sum_animal = 0
    for k, val in dict_animal.items():
        sum_animal += len(val)
        print(f'{k}: {len(val)}')
    print(sum_animal)

    # Запись решения (ответа) в текстовый файл
    with open('animal_name_count.txt', 'w') as f:
        for k, val in dict_animal.items():
            f.write(f'{k}: {len(val)} \n')


start_time = time.time()
parser()
print(f"parser: {time.time() - start_time} seconds ")  # 301 sec


"""
# Получаем список всех страниц
list_pages = get_list_pages(BASE_URL)

# Сохраняем список всех страниц в файл .txt
save_list_txt(list_pages, 'list_pages')

# Получаем список всех страниц из файла .txt
# list_pages = get_list_txt('list_pages')

# Получаем словарь с именами всех животных со всех страниц
dict_animal = get_dict_all_animal(list_pages)

# Сохраняем словарь в файл .json
save_dict_json(dict_animal, 'dict_animal')

# Получаем словарь с именами всех животных из файла .json
# dict_animal = get_dict_json('dict_animal')

# Обычный вывод решения (ответа) по условиям задачки
sum_animal = 0
for k, val in dict_animal.items():
    sum_animal += len(val)
    print(f'{k}: {len(val)}')
print(sum_animal)

# Запись решения (ответа) в текстовый файл
with open('animal_name_count.txt', 'w') as f:
    for k, val in dict_animal.items():
        f.write(f'{k}: {len(val)} \n')
"""
