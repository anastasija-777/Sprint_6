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

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.step('Открываем страницу {URL.basa_url}')
@pytest.fixture(scope='function')
def open(driver):
    driver.get(URL.basa_url)

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def order_page_for_whom(driver):
    return OrderPageForWhom(driver)

@pytest.fixture(scope='function')
def order_page_rental(driver):
    return OrderPageRental(driver)

@pytest.fixture(scope='function')
def basa_page(driver):
    return BasaPage(driver)

@pytest.fixture(scope='function')
def button_cookie(driver):
    driver.find_element(*MainPageLocators.BUTTON_COOKIE_LOCATOR).click()





