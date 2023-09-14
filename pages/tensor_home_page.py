from selenium.webdriver.common.by import By

from .base_page import BasePage


class TensorHomePage(BasePage):
    """
    PageObject класс для главной страницы tensor.ru.
    """

    POWER_IN_PEOPLE_BLOCK = (
        By.XPATH,
        "//div[contains(text(), 'Сила в людях')]",
    )
    POWER_IN_PEOPLE_MORE_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Подробнее')]",
    )

    def open_power_in_people_page(self):
        """
        Открывает страницу "Сила в людях" на tensor.ru.
        """
        self.find_element(self.POWER_IN_PEOPLE_BLOCK).click()
        self.find_element(
            self.POWER_IN_PEOPLE_MORE_LINK
        ).click()


# .tensor_ru-About__block3-image-filter
