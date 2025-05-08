import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import URL
from pages.main_page import MainPage
from locators.main_page_locator import MainPageLocators
from pages.order_page_for_whom import OrderPageForWhom
from pages.order_page_rental import OrderPageRental
from pages.basa_page import BasaPage

@allure.step('Создаем драйвер Firefox и после выполнения всей действий закрываем браузер')
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.step('Открываем страницу {URL.basa_url}')
@pytest.fixture(scope='function')
def open(driver):
    driver.get(URL.basa_url)

@allure.step('Создаем объект главной страницы')
@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@allure.step('Создаем объект страницы формы заполнения "Для кого самокат"')
@pytest.fixture(scope='function')
def order_page_for_whom(driver):
    return OrderPageForWhom(driver)

@allure.step('Создаем объект страницы формы заполнения "Про аренду"')
@pytest.fixture(scope='function')
def order_page_rental(driver):
    return OrderPageRental(driver)

@allure.step('В всплывающем окне на главной странице нажимаем кнопку о принятии кук')
@pytest.fixture(scope='function')
def button_cookie(driver):
    driver.find_element(*MainPageLocators.BUTTON_COOKIE_LOCATOR).click()





