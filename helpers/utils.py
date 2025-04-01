import random

import allure


@allure.step("Генерируем Post Code")
def generate_post_code() -> str:
    return "".join(str(random.randint(1, 9)) for _ in range(10))


@allure.step("Генерируем First Name на основе Post Code")
def generate_first_name(post_code):
    name = ""
    for i in range(0, len(post_code), 2):
        num = int(post_code[i:i+2])
        letter = chr(97 + (num % 26))
        name += letter
    return name


@allure.step("Находим имя, длина которого ближе к среднему арифметическому")
def find_name_closer_to_avg_length(list_names):
    list_name_of_lengths = [len(name) for name in list_names]
    avg_length = sum(list_name_of_lengths) / len(list_name_of_lengths)
    name_selected_for_deletion = None
    min_difference = len(list_names[0])
    for name in list_names:
        difference = abs(len(name) - avg_length)
        if difference < min_difference:
            min_difference = difference
            name_selected_for_deletion = name
    return name_selected_for_deletion
