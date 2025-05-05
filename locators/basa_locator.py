import pytest
from selenium.webdriver.common.by import By


class BasaLocators:
    LOGO_SCOOTER_LOCATOR = By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]'
    YANDEX_LOCATOR = By.XPATH, './/img[@alt="Yandex"]'