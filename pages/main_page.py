import allure
from pages.basa_page import BasaPage
from locators.main_page_locator import MainPageLocators


class MainPage(BasaPage):

    @allure.step('Находим вопрос,кликаем и получаем ответ')
    def click_to_question_and_get_answer(self,locator_q,locator_a):
        self.find_element_with_wait(locator_q)
        self.click_on_element(locator_q)
        self.find_element_with_wait(locator_a)
        return self.get_text_from_element(locator_a)

    @allure.step('Проверка ответа на вопрос')
    def check_click_to_question_and_get_answer(self, locator_q,locator_a,answer):
        self.scroll_to_element(locator_q)
        result = self.click_to_question_and_get_answer(locator_q,locator_a)
        assert result == answer

    @allure.step('Кликаем по кнопке "Заказать" в заголовке')
    def click_button_order_in_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)

    @allure.step('Скроллим до кнопки "Заказать" под статусами')
    def scroll_to_element_button_after_statuses(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_AFTER_STATUSES_LOCATOR)

    @allure.step('Кликаем по кнопке "Заказать" под статусами')
    def click_button_after_statuses(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_AFTER_STATUSES_LOCATOR)
