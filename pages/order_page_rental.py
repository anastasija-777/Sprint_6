import allure
from pages.basa_page import BasaPage
from locators.order_page_rental_locator import OrderPageRentalLocators

class OrderPageRental(BasaPage):

    @allure.step('Находим поле "Когда привезти самокат" и выбираешь дату {rental_data}')
    def choice_when_to_bring_scooter(self,locator_cd,rental_data):  # выбор даты аренды
        self.find_element_with_wait(locator_cd).click()
        self.find_element_with_wait(rental_data).click()

    @allure.step('Находим поле "Срок аренды" и выбираешь срок {rental_period}')
    def choice_rental_period(self,locator_cp,rental_period):  # выбор срока аренды
        self.click_on_element(locator_cp)
        self.scroll_to_element(rental_period)
        self.click_on_element(rental_period)

    @allure.step('Находим поле "Цвет самоката" и выбираешь цвет {color}')
    def choice_color_scooter(self,locator_cc,color):   # выбор цвета самоката
        self.find_element_with_wait(locator_cc)
        self.click_on_element(color)

    @allure.step('Находим поле Комментарий и пишешь комментарий {comment}')
    def input_comment(self,locator_ic,comment):
        self.click_on_element(locator_ic)
        self.find_element_with_wait(locator_ic).send_keys(comment)

    @allure.step('Находим кнопку Заказать и кликаешь по ней')
    def button_order(self,locator_o):
        self.click_on_element(locator_o)

    @allure.step('Заполняем форму заказа "Про аренду" и кликаем по кнопке Заказать')
    def order_page_rental(self,rental_data,rental_period,color,comment):
        self.choice_when_to_bring_scooter(OrderPageRentalLocators.CHOICE_DATE_LOCATOR,rental_data)
        self.choice_rental_period(OrderPageRentalLocators.CHOICE_RENTAL_PERIOD_LOCATOR,rental_period)
        self.choice_color_scooter(OrderPageRentalLocators.CHOICE_COLOR_SCOOTER_LOCATOR, color)
        self.input_comment(OrderPageRentalLocators.INPUT_COMMENT_LOCATOR, comment)
        self.button_order(OrderPageRentalLocators.BUTTON_ORDER_LOCATOR)

    @allure.step('Переходим на следующую страницу заполнения формы "Про аренду"')
    def page_form_order_rental(self):
        self.find_element_with_wait(OrderPageRentalLocators.CHOICE_DATE_LOCATOR)

    @allure.step('В всплывающем окне "Хотите оформить заказ?" кликаем по кнопке Да')
    def click_button_yes(self):
        self.click_on_element(OrderPageRentalLocators.BUTTON_YES_LOCATOR)

    @allure.step('Проверяем что заказ успешно оформлен')
    def check_successful_order(self):
        element = self.find_element_with_wait(OrderPageRentalLocators.TEXT_ORDER_LOCATOR)
        text = element.text[0:14]
        assert  text == 'Заказ оформлен'

    @allure.step('В всплывающем окне "Заказ оформлен" кликаем по кнопке "Посмотреть статус')
    def click_button_view_status(self):
        self.click_on_element(OrderPageRentalLocators.BUTTON_VIEW_STATUS_LOCATOR)


