import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import main_page
from data import URL
from data import Data
from locators.main_page_locator import MainPageLocators



class TestClickToQuestionAndGetAnswer:

    @allure.title('Проверка ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def test_click_to_question_and_get_answer_0(self,driver,open, main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_0,
                                                         MainPageLocators.ANSWER_LOCATOR_0,
                                                         Data.expected_answer_0)

    @allure.title('Проверка ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def test_click_to_question_and_get_answer_1(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_1,
                                                         MainPageLocators.ANSWER_LOCATOR_1,
                                                         Data.expected_answer_1)

    @allure.title('Проверка ответа на вопрос "Как рассчитывается время аренды?"')
    def test_click_to_question_and_get_answer_2(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_2,
                                                         MainPageLocators.ANSWER_LOCATOR_2,
                                                         Data.expected_answer_2)

    @allure.title('Проверка ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_click_to_question_and_get_answer_3(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_3,
                                                         MainPageLocators.ANSWER_LOCATOR_3,
                                                         Data.expected_answer_3)

    @allure.title('Проверка ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_click_to_question_and_get_answer_4(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_4,
                                                         MainPageLocators.ANSWER_LOCATOR_4,
                                                         Data.expected_answer_4)

    @allure.title('Проверка ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_click_to_question_and_get_answer_5(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_5,
                                                         MainPageLocators.ANSWER_LOCATOR_5,
                                                         Data.expected_answer_5)

    @allure.title('Проверка ответа на вопрос "Можно ли отменить заказ?"')
    def test_click_to_question_and_get_answer_6(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_6,
                                                         MainPageLocators.ANSWER_LOCATOR_6,
                                                         Data.expected_answer_6)

    @allure.title('Проверка ответа на вопрос "Я жизу за МКАДом, привезёте?"')
    def test_click_to_question_and_get_answer_7(self,driver,open,main_page,button_cookie):
        main_page.check_click_to_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR_7,
                                                         MainPageLocators.ANSWER_LOCATOR_7,
                                                         Data.expected_answer_7)




