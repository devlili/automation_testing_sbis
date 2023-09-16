from selenium.webdriver.common.by import By


class SbisContactsLocators:
    CONTACTS_SECTION = (By.XPATH, "//h2[text()='Контакты']")
    REGION_NAME = (
        By.CSS_SELECTOR,
        "span.sbis_ru-Region-Chooser__text.sbis_ru-link",
    )
    REGION_SELECT = (By.CLASS_NAME, "sbis_ru-Region-Chooser.ml-16.ml-xm-0")
    PARTNERS_LIST = (By.CSS_SELECTOR, "div[name='itemsContainer']")
    TENSOR_PAGE = (By.XPATH, "//a[@title='tensor.ru']")


class SbisHomeLocators:
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    DOWNLOAD_SBIS = (By.LINK_TEXT, "Скачать СБИС")
    PLAGIN = (By.XPATH, "//div[text()='СБИС Плагин']")
    WINDOWS = (
        By.XPATH,
        "//span[contains(@class, 'js-innerTabPlugin') and text()='Windows']",
    )
    WEB_INSTALLER = (
        By.XPATH,
        "//a[contains(text(), 'Скачать (Exe 3.64 МБ)')]",
    )


class TensorHomeLocators:
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    POWER_IN_PEOPLE_MORE_LINK = (
        By.CSS_SELECTOR,
        "a.tensor_ru-link[href='/about']",
    )


class TensorAboutLocators:
    WORKING_SECTION = (By.XPATH, "//h2[text()='Работаем']")
    IMAGE = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']")
