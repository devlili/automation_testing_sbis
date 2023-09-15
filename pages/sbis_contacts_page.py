from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import SbisContactsLocators


class SbisContactsPage(BasePage):
    """PageObject класс для страницы "Контакты" на sbis.ru."""

    def select_region(self, region):
        """Выбирает регион на странице "Контакты"."""

        region_select = self.find_element(SbisContactsLocators.REGION_SELECT)
        region_select.click()
        region_option = region_select.find_element(
            By.XPATH, f"//option[text()='{region}']"
        )
        region_option.click()

    def get_partners_list(self):
        """Получает текст списка партнеров на странице "Контакты"."""

        return self.find_element(SbisContactsLocators.PARTNERS_LIST).text
