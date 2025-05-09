import pytest
import allure
from data import Data


class TestOrderScooter:
    @allure.title('Проверяем что через кнопку "Заказать" вверху можно оформить заказ, через клик по логотипу «Самоката» можем вернуться на главную страницу «Самоката», через клик по логотипу Яндекса переходим на главную страницу Дзена')
    @pytest.mark.parametrize('name',['Ян','Оля','АнастасияНастя','АнастасияНастяЯ'])
    def test_order_scooter_button_order_in_header(self,driver,open, main_page, order_page_for_whom,order_page_rental,button_cookie,name):
        # кликаем по кнопке "Заказать" в заголовке
        main_page.click_button_order_in_header()
        # ожидаем переход на страницу заполнения формы "Для кого самокат"
        order_page_for_whom.page_form_order_for_whom()
        # заполняем форму заказа "Для кого самокат" и кликаем по кнопке Далее
        order_page_for_whom.input_order_page_for_whom(
            name,
            Data.data_set_for_whom_1['surname'],
            Data.data_set_for_whom_1['address'],
            Data.data_set_for_whom_1['metro_station'],
            Data.data_set_for_whom_1['phone_number']
        )
        # ожидаем переход на следующую страницу заполнения формы "Про аренду"
        order_page_rental.page_form_order_rental()
        # заполняем форму заказа "Про аренду" и кликаем по кнопке Заказать
        order_page_rental.order_page_rental(
            Data.data_set_rental_1['rental_data'],
            Data.data_set_rental_1['rental_period'],
            Data.data_set_rental_1['color'],
            Data.data_set_rental_1['comment']
        )
        # в всплывающем окне "Хотите оформить заказ?" кликаем по кнопке Да
        order_page_rental.click_button_yes()
        # Проверяем что вышло сообщение "Заказ оформлен"
        order_page_rental.check_successful_order()

        # в всплывающем окне "Заказ оформлен" кликаем по кнопке "Посмотреть статус'
        order_page_rental.click_button_view_status()
        # проверяем что при клике на логотип «Самоката» попадаем на главную страницу «Самоката».
        order_page_rental.check_click_logo_scooter_skip_main_page()

        # проверяем что при кликаем на логотип Яндекса происходит переход на главную страницу Дзена
        main_page.check_click_logo_yandex_skip_dzen()


    @allure.title('Проверяем что через кнопку "Заказать" внизу можно оформить заказ, через клик по логотипу «Самоката» можем вернуться на главную страницу «Самоката», через клик по логотипу Яндекса переходим на главную страницу Дзена')
    def test_order_scooter_button_order_after_statuses(self, driver, open, main_page, order_page_for_whom,
                                                   order_page_rental, button_cookie):
        # кликаем по кнопке "Заказать" под статусами
        main_page.scroll_to_element_button_after_statuses()
        main_page.click_button_after_statuses()
        main_page.click_button_order_in_header()
        # ожидаем переход на страницу заполнения формы "Для кого самокат"
        order_page_for_whom.page_form_order_for_whom()
        # заполняем форму заказа "Для кого самокат" и кликаем по кнопке Далее
        order_page_for_whom.input_order_page_for_whom(
            Data.data_set_for_whom_2['surname'],
            Data.data_set_for_whom_2['surname'],
            Data.data_set_for_whom_2['address'],
            Data.data_set_for_whom_2['metro_station'],
            Data.data_set_for_whom_2['phone_number']
        )
        # ожидаем переход на следующую страницу заполнения формы "Про аренду"
        order_page_rental.page_form_order_rental()
        # заполняем форму заказа "Про аренду" и кликаем по кнопке Заказать
        order_page_rental.order_page_rental(
            Data.data_set_rental_2['rental_data'],
            Data.data_set_rental_2['rental_period'],
            Data.data_set_rental_2['color'],
            Data.data_set_rental_2['comment']
        )
        # в всплывающем окне "Хотите оформить заказ?" кликаем по кнопке Да
        order_page_rental.click_button_yes()
        # Проверяем что вышло сообщение "Заказ оформлен"
        order_page_rental.check_successful_order()

        # в всплывающем окне "Заказ оформлен" кликаем по кнопке "Посмотреть статус'
        order_page_rental.click_button_view_status()
        # проверяем что при клике на логотип «Самоката» попадаем на главную страницу «Самоката».
        order_page_rental.check_click_logo_scooter_skip_main_page()

        # проверяем что при кликаем на логотип Яндекса происходит переход на главную страницу Дзена
        main_page.check_click_logo_yandex_skip_dzen()