import os

import pytest

from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_home_page import SbisHomePage


def test_open_download_page(browser):
    """Проверка перехода на страницу загрузок из Footer'а."""

    link = "https://sbis.ru"
    sbis_home_page = SbisHomePage(browser, link)
    sbis_home_page.go_to_site()
    sbis_home_page.go_to_download()
    sbis_download_page = SbisDownloadPage(browser, browser.current_url)
    sbis_download_page.should_be_download_page()


@pytest.mark.usefixtures("browser", "logger")
def test_scenario3(browser, logger):
    """Проверка скачивания СБИС Плагина и размера скачанного файла."""

    link = "https://sbis.ru/download?tab=plugin&innerTab=default"
    sbis_home_page = SbisDownloadPage(browser, link)
    sbis_home_page.go_to_site()
    sbis_home_page.download_sbis()
    logger.info(
        "Открыт СБИС Плагин для windows, началась загрузка веб-установщика"
    )

    downloads_folder = "downloads"
    file_name = "sbisplugin-setup-web.exe"
    file_path = os.path.join(os.getcwd(), downloads_folder, file_name)

    assert os.path.exists(file_path), "Файл не был скачан"
    logger.info("Файл скачан")

    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    expected_file_size_mb = 3.64

    assert (
        abs(file_size_mb - expected_file_size_mb) < 0.1
    ), "Неверный размер файла"
    logger.info("Тест успешно завершен")
