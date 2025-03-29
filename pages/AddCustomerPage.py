import allure
from helpers.BasePage import BasePage
from selenium.webdriver.common.by import By
from data.constants import TEXT_FIRST_NAME, TEXT_LAST_NAME, TEXT_POST_CODE


class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=10)
        self.first_name_input = (By.XPATH, "//input[@placeholder='First Name']")
        self.last_name_input = (By.XPATH, "//input[@placeholder='Last Name']")
        self.post_code_input = (By.XPATH, "//input[@placeholder='Post Code']")
        self.add_customer_btn = (By.XPATH, "//button[text()='Add Customer']")
    
    @allure.step(f"Добавляем данные клиента: {TEXT_FIRST_NAME}, {TEXT_LAST_NAME}, {TEXT_POST_CODE}")
    def add_customer(self, first_name: str, last_name: str, post_code: str) -> None:
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_post_code(post_code)
        self.add_customer_button_click()

    @allure.step(f"Ввод имени: {TEXT_FIRST_NAME}")
    def input_first_name(self, first_name: str) -> None:
        self.fill_field(self.first_name_input, first_name)

    @allure.step(f"Ввод фамилии: {TEXT_LAST_NAME}")
    def input_last_name(self, last_name: str) -> None:
        self.fill_field(self.last_name_input, last_name)

    @allure.step(f"Ввод почтового кода: {TEXT_POST_CODE}")
    def input_post_code(self, post_code: str) -> None:
        self.fill_field(self.post_code_input, post_code)

    @allure.step("Нажать кнопку 'Add Customer'")
    def add_customer_button_click(self) -> None:
        self.click_element(self.add_customer_btn)

    @allure.step("Получение текста из всплывающего окна")
    def get_alert_text(self) -> None:
        return self.driver.switch_to.alert.text

    @allure.step("Подтверждение и закрытие всплывающего окна")
    def accept_alert(self) -> None:
        self.driver.switch_to.alert.accept()
