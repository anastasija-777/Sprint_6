import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import URL
from data import Data
from locators.main_page_locator import MainPageLocators
from locators.order_page_for_whom_locator import OrderPageForWhomLocators
from locators.order_page_rental_locator import OrderPageRentalLocators
from locators.basa_locator import BasaLocators


class TestOrderScooter:
    @allure.title('Проверяем что через кнопку "Заказать" вверху можно оформить заказ, через клик по логотипу «Самоката» можем вернуться на главную страницу «Самоката», через клик по логотипу Яндекса переходим на главную страницу Дзена')
    @pytest.mark.parametrize('name',['Ян','Оля','АнастасияНастя','АнастасияНастяЯ'])
    def test_order_scooter_button_order_in_header(self,driver,open, basa_page,main_page, order_page_for_whom,order_page_rental,button_cookie,name):
        # кликаем по кнопке "Заказать" в заголовке
        main_page.click_button_order_in_header(MainPageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)
        # ожидаем переход на страницу заполнения формы "Для кого самокат"
        order_page_for_whom.page_form_order_for_whom(OrderPageForWhomLocators.INPUT_NAME_LOCATOR,
                                                     URL.order_url)
        # заполняем форму заказа "Для кого самокат" и кликаем по кнопке Далее
        order_page_for_whom.input_order_page_for_whom(
            OrderPageForWhomLocators.INPUT_NAME_LOCATOR,name,
            OrderPageForWhomLocators.INPUT_SURNAME_LOCATOR,Data.surname_1,
            OrderPageForWhomLocators.INPUT_ADDRESS_LOCATOR,Data.address_1,
            OrderPageForWhomLocators.INPUT_STATION_LOCATOR,OrderPageForWhomLocators.STATION_SOKOLNIKI_LOCATOR,
            OrderPageForWhomLocators.INPUT_PHONE_NUMBER_LOCATOR,Data.phone_number_1,
            OrderPageForWhomLocators.BUTTON_NEXT_LOCATOR)
        # ожидаем переход на следующую страницу заполнения формы "Про аренду"
        order_page_for_whom.find_element_with_wait(OrderPageRentalLocators.CHOICE_DATE_LOCATOR)
        # заполняем форму заказа "Про аренду" и кликаем по кнопке Заказать
        order_page_rental.order_page_rental(
            OrderPageRentalLocators.CHOICE_DATE_LOCATOR,OrderPageRentalLocators.DATE_FIVE_LOCATOR,
            OrderPageRentalLocators.CHOICE_RENTAL_PERIOD_LOCATOR,OrderPageRentalLocators.RENTAL_PERIOD_SEVEN_LOCATOR,
            OrderPageRentalLocators.CHOICE_COLOR_SCOOTER_LOCATOR,OrderPageRentalLocators.COLOR_SCOOTER_GREY_LOCATOR,
            OrderPageRentalLocators.INPUT_COMMENT_LOCATOR,Data.comment_1,
            OrderPageRentalLocators.BUTTON_ORDER_LOCATOR)
        # в всплывающем окне "Хотите оформить заказ?" кликаем по кнопке Да
        order_page_rental.click_button_yes(OrderPageRentalLocators.BUTTON_YES_LOCATOR)
        # Проверяем что вышло сообщение "Заказ оформлен"
        order_page_rental.check_successful_order(OrderPageRentalLocators.TEXT_ORDER_LOCATOR)

        # в всплывающем окне "Заказ оформлен" кликаем по кнопке "Посмотреть статус'
        order_page_rental.click_button_view_status(OrderPageRentalLocators.BUTTON_VIEW_STATUS_LOCATOR)
        # проверяем что при клике на логотип «Самоката» попадаем на главную страницу «Самоката».
        basa_page.check_click_logo_scooter_skip_main_page(BasaLocators.LOGO_SCOOTER_LOCATOR,
                                                         URL.basa_url)

        # проверяем что при кликаем на логотип Яндекса происходит переход на главную страницу Дзена
        basa_page.check_click_logo_yandex_skip_dzen(BasaLocators.YANDEX_LOCATOR,
                                                    URL.dzen_url)

    @allure.title('Проверяем что через кнопку "Заказать" внизу можно оформить заказ, через клик по логотипу «Самоката» можем вернуться на главную страницу «Самоката», через клик по логотипу Яндекса переходим на главную страницу Дзена')
    def test_order_scooter_button_order_after_statuses(self,driver,open, basa_page, main_page, order_page_for_whom,order_page_rental,button_cookie):
        # кликаем по кнопке "Заказать" под статусами
        element = main_page.find_element_with_wait(MainPageLocators.BUTTON_ORDER_AFTER_STATUSES_LOCATOR)
        driver.execute_script("arguments[0].scrollIntoView()", element)
        element.click()
        # ожидаем переход на страницу заполнения формы "Для кого самокат"
        order_page_for_whom.page_form_order_for_whom(OrderPageForWhomLocators.INPUT_NAME_LOCATOR,
                                                     URL.order_url)
        # заполняем форму заказа "Для кого самокат" и кликаем по кнопке Далее
        order_page_for_whom.input_order_page_for_whom(
            OrderPageForWhomLocators.INPUT_NAME_LOCATOR, Data.name_2,
            OrderPageForWhomLocators.INPUT_SURNAME_LOCATOR, Data.surname_2,
            OrderPageForWhomLocators.INPUT_ADDRESS_LOCATOR, Data.address_1,
            OrderPageForWhomLocators.INPUT_STATION_LOCATOR, OrderPageForWhomLocators.STATION_SOKOLNIKI_LOCATOR,
            OrderPageForWhomLocators.INPUT_PHONE_NUMBER_LOCATOR, Data.phone_number_1,
            OrderPageForWhomLocators.BUTTON_NEXT_LOCATOR)
        # ожидаем переход на следующую страницу заполнения формы "Про аренду"
        order_page_for_whom.find_element_with_wait(OrderPageRentalLocators.CHOICE_DATE_LOCATOR)
        # заполняем форму заказа "Про аренду" и кликаем по кнопке Заказать
        order_page_rental.order_page_rental(
            OrderPageRentalLocators.CHOICE_DATE_LOCATOR, OrderPageRentalLocators.DATE_FIVE_LOCATOR,
            OrderPageRentalLocators.CHOICE_RENTAL_PERIOD_LOCATOR, OrderPageRentalLocators.RENTAL_PERIOD_SEVEN_LOCATOR,
            OrderPageRentalLocators.CHOICE_COLOR_SCOOTER_LOCATOR, OrderPageRentalLocators.COLOR_SCOOTER_GREY_LOCATOR,
            OrderPageRentalLocators.INPUT_COMMENT_LOCATOR, Data.comment_1,
            OrderPageRentalLocators.BUTTON_ORDER_LOCATOR)
        # в всплывающем окне "Хотите оформить заказ?" кликаем по кнопке Да
        order_page_rental.click_button_yes(OrderPageRentalLocators.BUTTON_YES_LOCATOR)
        # Проверяем что вышло сообщение "Заказ оформлен"
        order_page_rental.check_successful_order(OrderPageRentalLocators.TEXT_ORDER_LOCATOR)

        # в всплывающем окне "Заказ оформлен" кликаем по кнопке "Посмотреть статус'
        order_page_rental.click_button_view_status(OrderPageRentalLocators.BUTTON_VIEW_STATUS_LOCATOR)
        # проверяем что при клике на логотип «Самоката» попадаем на главную страницу «Самоката».
        basa_page.check_click_logo_scooter_skip_main_page(BasaLocators.LOGO_SCOOTER_LOCATOR,
                                                          URL.basa_url)

        # проверяем что при кликаем на логотип Яндекса происходит переход на главную страницу Дзена
        basa_page.check_click_logo_yandex_skip_dzen(BasaLocators.YANDEX_LOCATOR,
                                                    URL.dzen_url)