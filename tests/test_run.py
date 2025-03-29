import allure

from data.constants import SUCCESS_MESSAGE
from helpers.utils import (find_name_closer_to_avg_length, generate_first_name,
                           generate_post_code)
from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage
from pages.ManagerPage import ManagerPage


@allure.epic('Тестирование банковского веб-сайта')
@allure.feature('Управление клиентами')
@allure.story('Добавление нового клиента')
class TestRun:
    @allure.title('Проверка добавления нового клиента')
    @allure.tag('UI', 'Создание клиента')
    @allure.description('''
    Шаги:
    1. Перейти на страницу 'Manager';
    2. Нажать на кнопку 'Add Customer';
    3. Сгенерировать тестовые данные (First Name, Last Name, Post Code);
    4. Заполнить пустые поля данными;
    5. Нажать кнопку 'Add Customer';
    6. Проверить появление всплывающего окна с подтверждением добавления;
    7. Закрыть всплывающее окно;
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка успешного добавления клиента')
    @allure.issue('Некорректное поведение при добавлении')
    def test_add_customer(self, browser) -> None:
        manager_page = ManagerPage(browser)
        manager_page.add_customer_section_click()
        add_customer_page = AddCustomerPage(browser)
        post_code = generate_post_code()
        first_name = generate_first_name(post_code)
        last_name = 'Holmes'
        add_customer_page.add_customer(first_name, last_name, post_code)
        alert_text = add_customer_page.get_alert_text()
        with allure.step('Проверяем текст из всплывающего окна'):
            assert SUCCESS_MESSAGE in alert_text, 'Клиент не добавлен!'
        add_customer_page.accept_alert()

    @allure.title('Проверка сортировки клиентов по имени')
    @allure.tag('UI', 'Сортировка')
    @allure.description('''
    Шаги:
    1. Перейти на страницу 'Manager';
    2. Нажать на вкладку "Customers";
    3. Получить изначальный список клиентов;
    4. Нажать на заголовок 'First Name' для сортировки;
    5. Получить отсортированный список клиентов;
    6. Проверить, что новый список отсортирован по имени.
    ''')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('Проверка успешной сортировки по имени')
    @allure.issue('Некорректное поведение при сортировке')
    def test_sort_customers_by_first_name(self, browser):
        manager_page = ManagerPage(browser)
        manager_page.customers_section_click()
        customers_page = CustomersPage(browser)
        initial_list_of_names = customers_page.get_list_customer_names()
        customers_page.sort_by_first_name()
        sorted_names = customers_page.get_list_customer_names()
        with allure.step(
            "Проверяем, что список клиентов отсортирован по имени"
        ):
            assert sorted_names == sorted(initial_list_of_names), \
                "Сортировка по имени не сработала!"

    @allure.title('Удаление клиента со средней длиной имени')
    @allure.tag('UI', 'Удаление')
    @allure.description('''
    Шаги:
    1. Перейти на страницу 'Manager';
    2. Нажать на вкладку 'Customers';
    3. Получить изначальный список клиентов;
    4. Найти имя, длина которого ближе к среднему арифметическому;
    5. Удалить найденного клиента;
    6. Проверить, что клиент больше не отображается в списке.
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка успешного удаления клиента')
    @allure.issue('Некорректное поведение при удалении')
    def test_delete_customer(self, browser):
        manager_page = ManagerPage(browser)
        manager_page.customers_section_click()
        customers_page = CustomersPage(browser)
        list_of_names_before_deletion = (
            customers_page.get_list_customer_names()
        )
        selected_name_to_delete = (
            find_name_closer_to_avg_length(list_of_names_before_deletion)
        )
        customers_page.delete_client_with_avg_length_name()
        list_of_names_after_deletion = customers_page.get_list_customer_names()
        with allure.step(
            f'Проверяем, что имя {selected_name_to_delete} удалено'
        ):
            assert selected_name_to_delete not in \
                list_of_names_after_deletion, 'Клиент не был удален!'
