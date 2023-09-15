import pytest
from selenium import webdriver

from utils.logger import configure_logger


@pytest.fixture(scope="module")
def browser():
    """Фикстура для создания экземпляра WebDriver."""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def logger():
    """Фикстура для создания экземпляра логгера."""

    return configure_logger()
