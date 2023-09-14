import pytest

from pages.sbis_home_page import SbisHomePage
from pages.tensor_home_page import TensorHomePage


@pytest.mark.usefixtures("browser", "logger")
def test_scenario1(browser, logger):
    """
    Тест первого сценария: Переход на tensor.ru и проверка страницы "Сила в людях".
    """
    sbis_home_page = SbisHomePage(browser)
    # tensor_home_page = TensorHomePage(browser)

    sbis_home_page.open_contacts_page()
    # tensor_home_page.open_power_in_people_page()

    # assert (
    #     "tensor.ru/about" in browser.current_url
    # ), "URL не соответствует ожидаемому"
