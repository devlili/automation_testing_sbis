from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import TensorHomeLocators


class TensorHomePage(BasePage):
    """PageObject класс для главной страницы tensor.ru."""

    def open_power_in_people_page(self):
        """Открывает страницу "Сила в людях" на tensor.ru."""

        self.find_element(TensorHomeLocators.POWER_IN_PEOPLE_BLOCK).click()
        self.find_element(TensorHomeLocators.POWER_IN_PEOPLE_MORE_LINK).click()


# .tensor_ru-About__block3-image-filter
