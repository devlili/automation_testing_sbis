from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Базовый класс для всех PageObject классов. Он содержит общие методы и
    атрибуты для всех страниц.
    """

    def __init__(self, driver, url):
        """
        Инициализирует объект класса BasePage.

        Параметры:
        - driver: Экземпляр веб-драйвера.
        - url: URL страницы, к которой будет осуществлено подключение.
        """
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
        """
        Ищет и возвращает первый найденный элемент на странице с заданным локатором.

        Параметры:
        - locator: Локатор элемента.
        - time: Время ожидания в секундах (по умолчанию 10).

        Возвращает:
        - Найденный элемент.

        Исключения:
        - TimeoutException, если элемент не был найден в течение указанного времени.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        """
        Ищет и возвращает все найденные элементы на странице с заданным локатором.

        Параметры:
        - locator: Локатор элементов.
        - time: Время ожидания в секундах (по умолчанию 10).

        Возвращает:
        - Список найденных элементов.

        Исключения:
        - TimeoutException, если элементы не были найдены в течение указанного времени.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def go_to_site(self):
        """
        Переходит на URL страницы, указанный при создании объекта класса BasePage.
        """
        return self.driver.get(self.url)

    def is_element_present(self, locator):
        """
        Проверяет наличие элемента на странице с заданным локатором.

        Параметры:
        - locator: Локатор элемента.

        Возвращает:
        - True, если элемент присутствует на странице, иначе False.
        """
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True
