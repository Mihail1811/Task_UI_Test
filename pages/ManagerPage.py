import allure
from selenium.webdriver.common.by import By

from helpers.BasePage import BasePage


class ManagerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=10)
        self.add_customer_btn = (By.XPATH, "//button[@ng-class='btnClass1']")
        self.customers_btn = (By.XPATH, "//button[@ng-class='btnClass3']")

    @allure.step("Нажать на секцию 'Add Customer'")
    def add_customer_section_click(self) -> None:
        self.click_element(self.add_customer_btn)

    @allure.step("Нажать на секцию 'Customers'")
    def customers_section_click(self) -> None:
        self.click_element(self.customers_btn)
