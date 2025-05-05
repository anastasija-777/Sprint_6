import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basa_page import BasaPage



class OrderPageRental(BasaPage):

    def choice_when_to_bring_scooter(self,locator_cd,locator_d):  # выбор даты аренды
        self.find_element_with_wait(locator_cd).click()
        self.find_element_with_wait(locator_d).click()

    def choice_rental_period(self,locator_cp,locator_s):  # выбор срока аренды
        self.click_on_element(locator_cp)
        element = self.find_element_with_wait(locator_s)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.click()

    def choice_color_scooter(self,locator_cc,locator_c):   # выбор цвета самоката
        self.find_element_with_wait(locator_cc)
        self.click_on_element(locator_c)

    def input_comment(self,locator_ic,comment):
        self.click_on_element(locator_ic)
        self.find_element_with_wait(locator_ic).send_keys(comment)

    def button_order(self,locator_o):
        self.click_on_element(locator_o)

    @allure.step('Заполняем форму заказа "Про аренду" и кликаем по кнопке Заказать')
    def order_page_rental(self,locator_cd,locator_d,locator_cp,locator_s,locator_cc,locator_c,locator_ic,comment,locator_o):
        self.choice_when_to_bring_scooter(locator_cd,locator_d)
        self.choice_rental_period(locator_cp,locator_s)
        self.choice_color_scooter(locator_cc, locator_c)
        self.input_comment(locator_ic, comment)
        self.button_order(locator_o)

    @allure.step('Переходим на следующую страницу {url} заполнения формы')
    def page_form_order_rental(self, locator, url):
        self.find_element_with_wait_url(locator, url)

    @allure.step('В всплывающем окне "Хотите оформить заказ?" кликаем по кнопке Да')
    def click_button_yes(self,locator):
        self.click_on_element(locator)

    @allure.step('Проверяем что заказ успешно оформлен')
    def check_successful_order(self,locator):
        element = self.find_element_with_wait(locator)
        text = element.text[0:14]
        assert  text == 'Заказ оформлен'

    @allure.step('В всплывающем окне "Заказ оформлен" кликаем по кнопке "Посмотреть статус')
    def click_button_view_status(self, locator):
        self.click_on_element(locator)


