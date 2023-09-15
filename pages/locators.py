from selenium.webdriver.common.by import By


class SbisContactsLocators:
    REGION_SELECT = (By.NAME, "region")
    PARTNERS_LIST = (By.CLASS_NAME, "partner-list")


class SbisHomeLocators:
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")


# div.sbisru-Header__container.sbis_ru-container:nth-child(2) li:nth-child(2) a


class TensorHomeLocators:
    POWER_IN_PEOPLE_BLOCK = (
        By.XPATH,
        "//div[contains(text(), 'Сила в людях')]",
    )
    POWER_IN_PEOPLE_MORE_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Подробнее')]",
    )
