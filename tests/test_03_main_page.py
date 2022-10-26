from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import *
from pages.order_page import *

@allure.suite("Тестирование переходов на главной странице")
class TestMainPage():

    driver = None

    @allure.title('1. Проверка перехода на страницу создания заказа на самокат')
    def test_order_page_open_via_header(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке оформления заказа в header"):
            MainPage(self.driver).get_main_page_and_order_via_header_button()
        with allure.step("Проверяем, что форма оформления заказа открылась"):
            assert self.driver.current_url == MainPageLocators.main_link + OrderPageLocators.order_link

    @allure.title('2. Проверка перехода на страницу создания заказа на самокат')
    def test_order_page_open_via_body(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке оформления заказа в body"):
            MainPage(self.driver).get_main_page_and_order_via_middle_button()
        with allure.step("Проверяем, что форма оформления заказа открылась"):
            assert self.driver.current_url == MainPageLocators.main_link + OrderPageLocators.order_link

    @allure.title('3. Проверка перехода на главную страницу сайта заказа самокатов, через переход в форму оформления заказа')
    def test_scooter_page_open_via_header(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке оформления заказа в header"):
            MainPage(self.driver).click_header_order_button()
        with allure.step("Клик по названию сайта 'Самокат' в header"):
            MainPage(self.driver).open_scooter_logo_button()
        with allure.step("Проверяем, что произошел переход на главную страницу сайта с заказом самокатов"):
            assert self.driver.current_url == MainPageLocators.main_link

    @allure.title('4. Проверка перехода на главную страницу сайта заказа самокатов, через страницу статуса заказа')
    def test_scooter_page_open_via_status(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке 'Статус'"):
            MainPage(self.driver).click_status_button()
        with allure.step("Клик по названию сайта 'Самокат' в header"):
            MainPage(self.driver).open_scooter_logo_button()
        with allure.step("Проверяем, что произошел переход на главную страницу сайта с заказом самокатов"):
            assert self.driver.current_url == MainPageLocators.main_link

    @allure.title('5. Проверка перехода на главную Яндекс через клик по логотипу Яндекс')
    def test_yandex_page_open(self, browser_setup):
        self.driver = browser_setup
        with allure.step("Клик по кнопке логотип Яндекса"):
            MainPage(self.driver).open_yandex_logo_button()
        with allure.step("Переключаем на вторую вкладку вкладку"):
            self.driver.switch_to.window(self.driver.window_handles[1])
        with allure.step(f"Проверяем, что URL на второй вкладке соответсвует: {MainPageLocators.dzen_link}"):
            WebDriverWait(self.driver, delay).until(EC.url_contains(MainPageLocators.dzen_link))
            assert self.driver.current_url == MainPageLocators.dzen_link

