from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import SbisContactsLocators


class SbisContactsPage(BasePage):
    """PageObject класс для страницы "Контакты" на sbis.ru."""

    def open_tensor_page(self):
        """Переходит по баннеру Тензор на страницу tensor.ru."""
        self.find_element(SbisContactsLocators.TENSOR_PAGE).click()

    def select_region(self, region):
        """Выбирает регион на странице "Контакты"."""
        self.find_element(SbisContactsLocators.REGION_SELECT).click()
        self.find_element((By.XPATH, f"//span[@title='{region}']")).click()

    def should_be_contacts_page(self):
        """Проверка наличия раздела Контакты."""
        assert self.is_element_present(
            SbisContactsLocators.CONTACTS_SECTION
        ), "Отсутсвует раздел Контакты"

    def get_name_region(self):
        """Получает название региона на странице "Контакты"."""
        return self.find_element(SbisContactsLocators.REGION_NAME).text

    def get_partners_list(self):
        """Получает текст списка партнеров на странице "Контакты"."""
        return self.find_element(SbisContactsLocators.PARTNERS_LIST).text
