from .base_page import BasePage
from .locators import TensorHomeLocators


class TensorHomePage(BasePage):
    """PageObject класс для главной страницы tensor.ru."""

    def should_be_power_in_people_block(self):
        """Проверка, что имеется блок "Сила в людях"."""

        assert self.is_element_present(
            TensorHomeLocators.POWER_IN_PEOPLE_BLOCK
        ), "блок 'Сила в людях' отсутствует"

    def open_power_in_people_page(self):
        """Открывает страницу Подробнее в "Сила в людях"."""

        element = self.find_element(
            TensorHomeLocators.POWER_IN_PEOPLE_MORE_LINK
        )
        self.driver.execute_script("arguments[0].click();", element)
