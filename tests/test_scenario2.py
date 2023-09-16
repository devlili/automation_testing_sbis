import time

import pytest

from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_home_page import SbisHomePage


@pytest.mark.usefixtures("browser", "logger")
def test_contacts_my_region(browser, logger):
    """Проверка своего региона в разделе "Контакты"."""

    link = "https://sbis.ru/"
    sbis_home_page = SbisHomePage(browser, link)
    sbis_contacts_page = SbisContactsPage(browser, link)

    sbis_home_page.open_contacts_page()

    partners_list = sbis_contacts_page.get_partners_list()
    name_region = sbis_contacts_page.get_name_region()

    assert (
        "Республика Башкортостан" in name_region
    ), f"Ожидался регион 'Республика Башкортостан', но получено: {name_region}"
    assert (
        "Уфа" in partners_list
    ), f"Cписок партнеров не получен, получено: {partners_list}"
    assert (
        "Республика Башкортостан" in browser.title
    ), "Заголовок страницы не соответствует ожидаемому"
    assert (
        "respublika-bashkortostan" in browser.current_url
    ), "URL не соответствует ожидаемому"


@pytest.mark.usefixtures("browser", "logger")
def test_contacts_other_region(browser, logger):
    """Проверка региона "Камчатский край" в разделе "Контакты"."""

    link = "https://sbis.ru/"
    sbis_home_page = SbisHomePage(browser, link)
    sbis_contacts_page = SbisContactsPage(browser, link)

    sbis_home_page.open_contacts_page()
    sbis_contacts_page.select_region("Камчатский край")

    time.sleep(2)
    partners_list = sbis_contacts_page.get_partners_list()
    name_region = sbis_contacts_page.get_name_region()

    assert (
        "Камчатский край" in name_region
    ), f"Ожидался регион 'Камчатский край', но получено: {name_region}"
    assert (
        "Камчатский" in partners_list
    ), f"Cписок партнеров неверный, получено: {partners_list}"
    assert (
        "Камчатский край" in browser.title
    ), "Заголовок страницы не соответствует ожидаемому"
    assert (
        "kamchatskij-kraj" in browser.current_url
    ), "URL не соответствует ожидаемому"
