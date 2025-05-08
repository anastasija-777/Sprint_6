import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.basa_locator import BasaLocators
from data import URL

class BasaPage:

    @allure.step('Инициализация драйвера')
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Ожидаем когда появится и находим элемент {locator}')
    def find_element_with_wait(self,locator):   # ожидаем появление элемента на странице
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем перехода на страницу {url} и находим элемент {locator}')
    def find_element_with_wait_url(self,locator,url):   # ожидаем переход на новую страницу
        WebDriverWait(self.driver,30).until(expected_conditions.url_to_be(url))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу {locator}')
    def click_on_element(self,locator):   # кликаем по элементу
        element = self.driver.find_element(*locator)
        element.click()

    @allure.step('Получаем текст из элемента {locator}')
    def get_text_from_element(self,locator):   # получить текст из элемента
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Скроллим до элемента {locator}')
    def scroll_to_element(self, locator):  # получить текст из элемента
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)


    @allure.step('Кликаем на логотип «Самоката»')
    def click_logo_scooter(self):
        self.click_on_element(BasaLocators.LOGO_SCOOTER_LOCATOR)

    @allure.step('Проверяем что при кликаем на логотип «Самоката» происходит переход на главную страницу Самоката')
    def check_click_logo_scooter_skip_main_page(self):
        self.click_logo_scooter()
        assert self.driver.current_url == URL.basa_url

    @allure.step('Кликаем на логотип Яндекса')
    def click_logo_yandex(self):
        self.click_on_element(BasaLocators.YANDEX_LOCATOR)

    @allure.step('Проверяем что при кликаем на логотип Яндекса происходит переход на главную страницу Дзена')
    def check_click_logo_yandex_skip_dzen(self):
        self.click_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 30).until(expected_conditions.url_contains(URL.dzen_url))
        assert URL.dzen_url in self.driver.current_url


