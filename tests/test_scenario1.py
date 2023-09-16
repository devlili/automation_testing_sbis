import pytest

from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_home_page import SbisHomePage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_home_page import TensorHomePage

# @pytest.mark.usefixtures("browser", "logger")
# def test_scenario1(browser, logger):
#     """
#     Тест первого сценария: Переход на tensor.ru и проверка страницы "Сила в людях".
#     """
#     link = "https://sbis.ru/"
#     sbis_home_page = SbisHomePage(browser, link)
#     sbis_contacts_page = SbisContactsPage(browser, link)

#     sbis_home_page.open_contacts_page()
#     sbis_contacts_page.open_tensor_page()

#     tensor_home_page = TensorHomePage(browser, "https://tensor.ru/")
#     tensor_home_page.should_be_power_in_people_block()

# assert (
#     "tensor.ru" in browser.current_url
# ), "URL не соответствует ожидаемому"


def test_open_contacts(browser):
    """Проверка перехода в раздел Контакты."""

    link = "https://sbis.ru/"
    sbis_home_page = SbisHomePage(browser, link)
    sbis_home_page.open_contacts_page()
    contacts_block = SbisContactsPage(browser, browser.current_url)
    contacts = contacts_block.get_contacts_element()
    assert contacts.is_displayed(), "Нет раздела 'Контакты'"


# def test_open_tensor_from_contacts(browser):
#     link = "https://sbis.ru/"
#     sbis_home_page = SbisHomePage(browser, link)
#     sbis_home_page.open_contacts_page()
#     sbis_contacts_page = SbisContactsPage(browser, browser.current_url)
#     sbis_contacts_page.open_tensor_page()
#     assert "https://tensor.ru/" in browser.current_url


def test_power_in_people_block(browser):
    """Проверка, что имеется блок "Сила в людях"."""

    link = "https://tensor.ru/"
    tensor_home_page = TensorHomePage(browser, link)
    tensor_home_page.go_to_site()
    tensor_home_page.should_be_power_in_people_block()


def test_open_about_from_tensor(browser):
    """Проверка перехода в "Подробнее" блока "Сила в людях"."""

    link = "https://tensor.ru/"
    tensor_home_page = TensorHomePage(browser, link)
    tensor_home_page.go_to_site()
    tensor_home_page.open_power_in_people_page()
    assert "https://tensor.ru/about" == browser.current_url


def test_working_section_images(browser):
    """Проверка высоты и ширины изображений раздела "Работаем"."""

    link = "https://tensor.ru/about"
    tensor_about_page = TensorAboutPage(browser, link)
    tensor_about_page.go_to_site()
    tensor_about_page.should_be_working_block()
    tensor_about_page.should_be_same_height_and_width_photos()
