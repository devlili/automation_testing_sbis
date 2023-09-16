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

        region_select = self.find_element(SbisContactsLocators.REGION_SELECT)
        region_select.click()
        self.find_element(
            (
                By.XPATH,
                f"//li[@class='sbis_ru-Region-Panel__item']/span[@title='{region}']",
            )
        ).click()

    def get_contacts_element(self):
        """Получает раздел Контакты."""
        return self.find_element(SbisContactsLocators.CONTACTS_SECTION)

    def get_name_region(self):
        """Получает название региона на странице "Контакты"."""
        return self.find_element(SbisContactsLocators.REGION_NAME).text

    def get_partners_list(self):
        """Получает текст списка партнеров на странице "Контакты"."""
        return self.find_element(SbisContactsLocators.PARTNERS_LIST).text
