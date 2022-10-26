import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import *
from pages.order_page import *

@allure.suite("Тестирование блока оформления заказа")
class TestOrderPage():

    driver = None

    @allure.title("1. Проверка создания заказа на самокат, через кнопку 'Заказать' в header сайта")
    def test_positive_order_via_header_button(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке 'Заказать' в header"):
            MainPage(self.driver).click_header_order_button()
        with allure.step("Заполняем форму заказа:"):
            OrderPage(self.driver).create_order_one_day(name="Павел",
                                                        surname="Неробов",
                                                        address="Минск",
                                                        phone="+79119910382",
                                                        comment="Спасибо")
        with allure.step("Проверяем, что форма заказа заполнена и открылась модалка после оформления заказа"):
            assert self.driver.find_element(*OrderPageLocators.complite_order_modal_window_displayed).is_displayed()
            MainPage(self.driver.get(MainPageLocators.main_link))

    @allure.title("2. Проверка создания заказа на самокат, через кнопку 'Заказать' в теле сайта")
    def test_positive_order_via_page_button(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке 'Заказать' в body"):
            MainPage(self.driver).click_body_order_button()
        with allure.step("Заполняем форму заказа:"):
            OrderPage(self.driver).create_order_five_day(name="Пабло",
                                                        surname="Никробиус",
                                                        address="Москва",
                                                        subway="ав",
                                                        phone="+79919110382")
        with allure.step("Проверяем, что форма заказа заполнена и открылась модалка после оформления заказа"):
            assert self.driver.find_element(*OrderPageLocators.complite_order_modal_window_displayed).is_displayed()
            MainPage(self.driver.get(MainPageLocators.main_link))


