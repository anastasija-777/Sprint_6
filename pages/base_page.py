import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

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

    @allure.step('Ожидаем перехода на страницу url которой содержит {url}')
    def find_element_with_wait_contains_url(self, url):  # ожидаем переход на новую страницу
        WebDriverWait(self.driver, 30).until(expected_conditions.url_contains(url))


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

    @allure.step('Ожидаем открытие новой вкладки')
    def switch_to_new_tab_with_wait(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Проверяем что текущий url содержит {url}')
    def check_find_element_contains_url(self,url):
        assert url in self.driver.current_url

    @allure.step('Проверяем что текущий url содержит {url}')
    def check_url(self, url):
        assert self.driver.current_url == url




