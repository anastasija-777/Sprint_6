import pytest
import allure
from conftest import main_page
from data import Data
from locators.main_page_locator import MainPageLocators



class TestClickToQuestionAndGetAnswer:

    @allure.title('Проверка ответа {expected_answer} на вопрос {question}')
    @pytest.mark.parametrize('question,answer,expected_answer',[
                             [MainPageLocators.QUESTION_LOCATOR_0,MainPageLocators.ANSWER_LOCATOR_0,Data.expected_answer_0],
                             [MainPageLocators.QUESTION_LOCATOR_1,MainPageLocators.ANSWER_LOCATOR_1,Data.expected_answer_1],
                             [MainPageLocators.QUESTION_LOCATOR_2,MainPageLocators.ANSWER_LOCATOR_2,Data.expected_answer_2],
                             [MainPageLocators.QUESTION_LOCATOR_3,MainPageLocators.ANSWER_LOCATOR_3,Data.expected_answer_3],
                             [MainPageLocators.QUESTION_LOCATOR_4,MainPageLocators.ANSWER_LOCATOR_4,Data.expected_answer_4],
                             [MainPageLocators.QUESTION_LOCATOR_5,MainPageLocators.ANSWER_LOCATOR_5,Data.expected_answer_5],
                             [MainPageLocators.QUESTION_LOCATOR_6,MainPageLocators.ANSWER_LOCATOR_6,Data.expected_answer_6],
                             [MainPageLocators.QUESTION_LOCATOR_7,MainPageLocators.ANSWER_LOCATOR_7,Data.expected_answer_7],
                             ]
                             )
    def test_click_to_question_and_get_answer_0(self, driver, open, main_page, button_cookie,question,answer,expected_answer):
        main_page.check_click_to_question_and_get_answer(question,answer,expected_answer)





