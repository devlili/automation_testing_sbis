from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import SbisHomeLocators


class SbisHomePage(BasePage):
    """PageObject класс для главной страницы sbis.ru."""

    def open_contacts_page(self):
        """Открывает страницу "Контакты" на sbis.ru."""

        self.go_to_site()
        self.find_element(SbisHomeLocators.CONTACTS_LINK).click()
