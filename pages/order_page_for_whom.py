import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basa_page import BasaPage



class OrderPageForWhom(BasaPage):

    def input_name(self,locator_n,name):  # заполнение поля Имя
        self.find_element_with_wait(locator_n).send_keys(name)

    def input_surname(self,locator_s,surname):  # заполнение поля Фамилия
        self.find_element_with_wait(locator_s).send_keys(surname)

    def input_address(self,locator_a,address):    # заполнение поля Адрес
        self.find_element_with_wait(locator_a).send_keys(address)

    def input_metro_station(self,locator_input,locator_station):   # выбор станции метро из выпадающего списка в поле Станция метро
        self.find_element_with_wait(locator_input).click()
        element = self.find_element_with_wait(locator_station)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.click()

    def input_phone_number(self,locator_p,phone_number):   # заполнение поля номер телефона
        self.find_element_with_wait(locator_p).send_keys(phone_number)

    def click_button_next(self,locator_next):
        self.click_on_element(locator_next)

    @allure.step('Заполняем форму заказа "Для кого самокат" и кликаем по кнопке Далее')
    def input_order_page_for_whom(self,locator_n,name,locator_s,surname,locator_a,address,locator_input,locator_station,locator_p,phone_number,locator_next):
        self.input_name(locator_n,name)
        self.input_surname(locator_s,surname)
        self.input_address(locator_a,address)
        self.input_metro_station(locator_input,locator_station)
        self.input_phone_number(locator_p,phone_number)
        self.click_button_next(locator_next)

    @allure.step('Переходим на страницу {url} заполнения формы заказа')
    def page_form_order_for_whom(self,locator,url):
        self.find_element_with_wait_url(locator,url)
