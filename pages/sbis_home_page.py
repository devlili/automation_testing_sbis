from selenium.webdriver.common.by import By

from .base_page import BasePage


class SbisHomePage(BasePage):
    """
    PageObject класс для главной страницы sbis.ru.
    """

    CONTACTS_LINK = (By.LINK_TEXT, "Контакты") # div.sbisru-Header__container.sbis_ru-container:nth-child(2) li:nth-child(2) a

    def open_contacts_page(self):
        """
        Открывает страницу "Контакты" на sbis.ru.
        """
        self.go_to_site()
        self.find_element(self.CONTACTS_LINK).click()
