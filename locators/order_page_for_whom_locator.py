import pytest
from selenium.webdriver.common.by import By

class OrderPageForWhomLocators:
    INPUT_NAME_LOCATOR = By.XPATH,'.//input[@placeholder="* Имя"]'
    INPUT_SURNAME_LOCATOR = By.XPATH, './/input[@placeholder="* Фамилия"]'
    INPUT_ADDRESS_LOCATOR = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    INPUT_STATION_LOCATOR = By.XPATH, './/input[@placeholder="* Станция метро"]'
    STATION_SOKOLNIKI_LOCATOR = By.XPATH, './/button/div[text()="Сокольники"]'
    STATION_LUBYANKA_LOCATOR = By.XPATH, './/button/div[text()="Лубянка"]'
    INPUT_PHONE_NUMBER_LOCATOR = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'
    BUTTON_NEXT_LOCATOR = By.XPATH,'.//button[text()="Далее"]'
