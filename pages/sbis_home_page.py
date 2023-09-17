from .base_page import BasePage
from .locators import SbisHomeLocators


class SbisHomePage(BasePage):
    """PageObject класс для главной страницы sbis.ru."""

    def open_contacts_page(self):
        """Открывает страницу "Контакты" на sbis.ru."""
        self.go_to_site()
        self.find_element(SbisHomeLocators.CONTACTS_LINK).click()

    def go_to_download(self):
        """Переход на скачивание СБИС Плагина."""
        download_sbis_link = self.find_element(
            SbisHomeLocators.DOWNLOAD_SBIS
        )
        self.driver.execute_script("arguments[0].click();", download_sbis_link)
