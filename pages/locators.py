from selenium.webdriver.common.by import By


class SbisContactsLocators:
    CONTACTS_SECTION = (By.XPATH, "//h2[text()='Контакты']")
    PARTNERS_LIST = (By.CSS_SELECTOR, "div[name='itemsContainer']")
    TENSOR_PAGE = (By.XPATH, "//a[@title='tensor.ru']")
    REGION_SELECT = (By.CLASS_NAME, "sbis_ru-Region-Chooser.ml-16.ml-xm-0")
    REGION_NAME = (
        By.CSS_SELECTOR,
        "span.sbis_ru-Region-Chooser__text.sbis_ru-link",
    )


class SbisHomeLocators:
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")


class TensorHomeLocators:
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    POWER_IN_PEOPLE_MORE_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Подробнее')]",
    )
