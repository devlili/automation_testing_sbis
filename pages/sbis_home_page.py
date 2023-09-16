from .base_page import BasePage
from .locators import SbisHomeLocators


class SbisHomePage(BasePage):
    """PageObject класс для главной страницы sbis.ru."""

    def open_contacts_page(self):
        """Открывает страницу "Контакты" на sbis.ru."""

        self.go_to_site()
        self.find_element(SbisHomeLocators.CONTACTS_LINK).click()

    def download_sbis(self):
        """Скачивает СБИС Плагин."""

        element = self.find_element(SbisHomeLocators.DOWNLOAD_SBIS)
        self.driver.execute_script("arguments[0].click();", element)

        element1 = self.find_element(SbisHomeLocators.PLAGIN)
        self.driver.execute_script("arguments[0].click();", element1)

        self.find_element(SbisHomeLocators.WINDOWS).click()
        self.find_element(SbisHomeLocators.WEB_INSTALLER).click()
