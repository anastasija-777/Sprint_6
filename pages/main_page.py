import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basa_page import BasaPage



class MainPage(BasaPage):

    @allure.step('Находим вопрос,кликаем и получаем ответ')
    def click_to_question_and_get_answer(self,locator_q,locator_a):
        self.find_element_with_wait(locator_q)
        self.click_on_element(locator_q)
        self.find_element_with_wait(locator_a)
        return self.get_text_from_element(locator_a)

    @allure.step('Проверка ответа на вопрос')
    def check_click_to_question_and_get_answer(self, locator_q,locator_a,answer):
        element = self.find_element_with_wait(locator_q)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        result = self.click_to_question_and_get_answer(locator_q,locator_a)
        assert result == answer

    @allure.step('Кликаем по кнопке "Заказать" в заголовке')
    def click_button_order_in_header(self, locator_bh):
        self.click_on_element(locator_bh)

    @allure.step('Кликаем по кнопке "Заказать" под статусами')
    def click_button_after_statuses(self, locator_bs):
        self.click_on_element(locator_bs)
