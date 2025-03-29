import allure
from data.constants import TEXT_FIRST_NAME
from helpers.BasePage import BasePage
from helpers.utils import find_name_closer_to_avg_length
from selenium.webdriver.common.by import By
from typing import List


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=10)
        self.sort_by_name_btn = (By.XPATH, "//a[contains(text(), 'First Name')]")
        self.customer_names = (By.XPATH, "//td[@class='ng-binding'][1]")
        self.delete_btn = (By.XPATH, "//button[text()='Delete']")

    @allure.step(f"Нажимаем на заголовок {TEXT_FIRST_NAME} для сортировки")
    def sort_by_first_name(self) -> None:
        self.click_element(self.sort_by_name_btn)
        sorted_names = self.get_list_customer_names()
        if sorted_names == sorted(sorted_names, reverse=True):
            self.click_element(self.sort_by_name_btn)

    @allure.step("Получаем список имен клиентов")
    def get_list_customer_names(self) -> List[str]:
        list_of_names = self.find_elements(*self.customer_names)
        return [name.text for name in list_of_names]
    
    @allure.step("Удаляем клиента с тем именем, у которого длина будет ближе к среднему арифметическому")
    def delete_client_with_avg_length_name(self) -> None:
        list_of_names = self.get_list_customer_names()
        name_to_delete = find_name_closer_to_avg_length(list_of_names)
        delete_buttons = self.find_elements(*self.delete_btn)
        list_of_names = self.find_elements(*self.customer_names)
        for id, name in enumerate(list_of_names):
            if name.text == name_to_delete:
                delete_buttons[id].click()
                break
