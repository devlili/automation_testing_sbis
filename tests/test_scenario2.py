import pytest

from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_home_page import SbisHomePage


@pytest.mark.usefixtures("browser", "logger")
def test_scenario2(browser, logger):
    """
    Тест второго сценария: Выбор региона на странице "Контакты".
    """
    sbis_home_page = SbisHomePage(browser)
    sbis_contacts_page = SbisContactsPage(browser)

    sbis_home_page.open_contacts_page()
    sbis_contacts_page.select_region("Камчатский край")

    partners_list = sbis_contacts_page.get_partners_list()
    assert (
        "Камчатский край" in partners_list
    ), f"Ожидался регион 'Камчатский край', но получено: {partners_list}"
    assert (
        "Камчатский край" in browser.title
    ), "Заголовок страницы не соответствует ожидаемому"
    assert (
        "Камчатский край" in browser.current_url
    ), "URL не соответствует ожидаемому"

# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_visible_text("text") 
