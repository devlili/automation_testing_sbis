import time

from .base_page import BasePage
from .locators import SbisDownloadLocators


class SbisDownloadPage(BasePage):
    """PageObject класс для страницы загрузок на sbis.ru."""

    def download_sbis(self):
        """Скачивает СБИС Плагин."""
        self.find_element(SbisDownloadLocators.PLUGIN).click()
        self.find_element(SbisDownloadLocators.WINDOWS).click()
        self.find_element(SbisDownloadLocators.WEB_INSTALLER).click()
        time.sleep(5)

    def should_be_download_page(self):
        """Проверка наличия страницы загрузок."""
        assert self.is_element_present(
            SbisDownloadLocators.DOWNLOAD_HEADER
        ), "Отсутсвует страница загрузок"
