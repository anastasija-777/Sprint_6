import pytest
from selenium.webdriver.common.by import By

class OrderPageRentalLocators:
    CHOICE_DATE_LOCATOR = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    DATE_FIVE_LOCATOR = By.XPATH, '//div[@aria-label="Choose понедельник, 5-е мая 2025 г."]'  # выбор даты - пн. 5.05.25
    DATE_SIX_LOCATOR = By.XPATH, '//div[@aria-label="Choose понедельник, 6-е мая 2025 г."]'   # выбор даты - пн. 6.05.25
    CHOICE_RENTAL_PERIOD_LOCATOR = By.XPATH, '//div[text()="* Срок аренды"]'
    RENTAL_PERIOD_ONE_LOCATOR = By.XPATH, '//div[text()="сутки"]'   # выбор срока - сутки
    RENTAL_PERIOD_SEVEN_LOCATOR = By.XPATH, '//div[text()="семеро суток"]'   # выбор срока - семеро суток
    CHOICE_COLOR_SCOOTER_LOCATOR = By.XPATH, '//div[text()="Цвет самоката"]'
    COLOR_SCOOTER_GREY_LOCATOR = By.XPATH, '//label[@for="grey"]'  # выбор цвета самокат 'серая безысходность'
    COLOR_SCOOTER_BLACK_LOCATOR = By.XPATH, '//label[@for="black"]'   # выбор цвета самокат 'черный жемчуг'
    INPUT_COMMENT_LOCATOR = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    BUTTON_ORDER_LOCATOR = By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]'
    BUTTON_YES_LOCATOR = By.XPATH, '//button[text()="Да"]'
    TEXT_ORDER_LOCATOR = By.XPATH, '//div[text()="Заказ оформлен"]'    # текст об успешном оформлении заказа
    BUTTON_VIEW_STATUS_LOCATOR = By.XPATH, '//button[text()="Посмотреть статус"]'



