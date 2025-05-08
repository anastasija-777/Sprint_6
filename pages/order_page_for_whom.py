import allure
from pages.basa_page import BasaPage
from locators.order_page_for_whom_locator import OrderPageForWhomLocators
from data import URL


class OrderPageForWhom(BasaPage):

    @allure.step('Находим поле Имя и указываем {name}')
    def input_name(self, locator_n,name):  # заполнение поля Имя
        self.find_element_with_wait(locator_n).send_keys(name)

    @allure.step('Находим поле Фамилия и указываем {surname}')
    def input_surname(self,locator_s,surname):  # заполнение поля Фамилия
        self.find_element_with_wait(locator_s).send_keys(surname)

    @allure.step('Находим поле Адрес и указываем {address}')
    def input_address(self,locator_a,address):    # заполнение поля Адрес
        self.find_element_with_wait(locator_a).send_keys(address)

    @allure.step('Находим поле Станция метро,кликаем по нему, скроллим до {metro_station} и кликаем по ней')
    def input_metro_station(self,locator_input,metro_station):   # выбор станции метро из выпадающего списка в поле Станция метро
        self.click_on_element(locator_input)
        self.scroll_to_element(metro_station)
        self.click_on_element(metro_station)

    @allure.step('Находим поле Номер телефона и указываем {phone_number}')
    def input_phone_number(self,locator_p,phone_number):   # заполнение поля номер телефона
        self.find_element_with_wait(locator_p).send_keys(phone_number)

    @allure.step('Находим кнопку Далее и кликаем по ней')
    def click_button_next(self,locator_next):
        self.click_on_element(locator_next)

    @allure.step('Заполняем форму заказа "Для кого самокат" и кликаем по кнопке Далее')
    def input_order_page_for_whom(self,name,surname,address,metro_station,phone_number):
        self.input_name(OrderPageForWhomLocators.INPUT_NAME_LOCATOR,name)
        self.input_surname(OrderPageForWhomLocators.INPUT_SURNAME_LOCATOR,surname)
        self.input_address(OrderPageForWhomLocators.INPUT_ADDRESS_LOCATOR,address)
        self.input_metro_station(OrderPageForWhomLocators.INPUT_STATION_LOCATOR,metro_station)
        self.input_phone_number(OrderPageForWhomLocators.INPUT_PHONE_NUMBER_LOCATOR,phone_number)
        self.click_button_next(OrderPageForWhomLocators.BUTTON_NEXT_LOCATOR)

    @allure.step('Переходим на следующую страницу для заполнения формы заказа "Для кого самокат"')
    def page_form_order_for_whom(self):
        self.find_element_with_wait_url(OrderPageForWhomLocators.INPUT_NAME_LOCATOR,URL.order_url)
